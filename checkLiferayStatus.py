#! /usr/bin/env python

import httplib, subprocess, socket

host = 'localhost'
statuscode = 200
blockcode =''
retcode = subprocess.call("/sbin/iptables -L |grep webcache",shell=True)
to = ['user1@example.com', 'user2@example.com']

'''
Routine to block port
'''
def blockLR():
    checkBlock()
    print "blockLR retcode:", retcode
    if retcode == 0:
        print "Rule already in place, skipping..."
    else:
        blockcode = 1
        sendalert(blockcode)
        #print "If this wasn't debug, I'd add a rule to iptables"
        return subprocess.call("/sbin/iptables -A INPUT -i eth1 -p tcp --dport 8080 -m state --state NEW,ESTABLISHED -j REJECT",shell=True)

'''
Routine to unblock port
'''
def unblockLR(retcode):
    print "unblock retcode:",retcode
    if retcode == 0:
        print "Unblocked"
        blockcode = 0
        sendalert(blockcode)
        #print "If this wasn't debug, I'd delete the block from iptables"
        return subprocess.call("/sbin/iptables -D INPUT -i eth1 -p tcp --dport 8080 -m state --state NEW,ESTABLISHED -j REJECT",shell=True)

'''
Check status of the iptables rule
'''
def checkBlock():
    retcode
#    print "checkBlock retcode:", retcode
    return retcode

'''
Check response from Liferay
'''
def checkLRstatus():

    socket.setdefaulttimeout(20)

    try:
        conn = httplib.HTTPConnection(host, 8080)
        conn.set_debuglevel(0)
        conn.request("GET","/web/guest")
        r1 = conn.getresponse()
        data = r1.read()
        host + ":" , r1.status, r1.reason,'\n' , r1.msg
        conn.close()

        #print "Status code:", type(statuscode), "r1.status", type(r1.status), "r1.reason", r1.reason

        if r1.status <> statuscode:
            print "not", statuscode ,", it's " + r1.status
            blockLR()
        else:
            print "UP: Status " + str(r1.status),"\n"
            checkBlock()
            unblockLR(retcode)

    except:
        print "Could not connect to" , host , "\n"
        blockLR()

'''
Send email - code paraphrased from: http://docs.python.org/2/library/email-examples.html
'''

def sendalert(blockcode):


    #print "sendalert blockcode:", blockcode

    import smtplib, socket
    from email.MIMEText import MIMEText

    server = 'smtp.example.com'
    ip = socket.gethostbyname_ex(socket.gethostname())
    sender = 'liferay.monitor@ogilvy.com'

    if blockcode == 1:
        msgtxt = 'To prevent login problems, Liferay is currently blocked on node ' + ip[2][0] + '\nTo unblock, run iptables -F'
        msgsubject = 'Port 8080 has been Blocked on ' + ip[2][0]
    else:
        msgtxt = 'Liferay has been unblocked on node ' + ip[2][0]
        msgsubject = 'Port 8080 has been UN-Blocked on ' + ip[2][0]

#    print "msgtxt:", msgtxt
#    print "msgsub:", msgsubject

    msg = MIMEText(msgtxt)
    msg['Subject'] = msgsubject
    msg['From'] = sender
    msg['To'] = ','.join(to)

    s = smtplib.SMTP()
    s.connect(server,25)
    s.sendmail(sender, to, msg.as_string())
    s.close()

checkLRstatus()
