#!/usr/bin/env python

import nmap
import json
import datetime
import socket
import os
import dns.resolver
import Queue
import threading
import time

# Required - nmap.py - https://code.google.com/p/python-nmap/source/browse/nmap/nmap.py

# Start config#
hosts       = '192.168.1.0/24'
threadCount = 10
# End config #

nm = nmap.PortScanner()
queue = Queue.Queue()
    
#ptr = ''

# Constructs the ptr record to search for in dns, e.g. '1.162.6.10.in-addr.arpa'
def getPTRvalue(sub1k):
    ptr = sub1k.split('.')
    ptr = ptr[3] + '.' + ptr[2] + '.' + ptr[1] + '.' + ptr[0] +'.in-addr.arpa'
    print "ptr", ptr
    try:
        ptr = dns.resolver.query(ptr, 'PTR')
        if len(ptr):
            print "Number of records:", len(ptr)
            for rec in ptr:
                print "rec" , rec , type(rec)
                rec = str(rec)
    except dns.resolver.NXDOMAIN:
        print "no ptr record for", ptr

    return ptr

# Function to run the nmap
def runScan(target):
    res = nm.scan(hosts= target, ports="1-65535", arguments='-A -sV -n -T4')
    for mainkey,mainvalue in res.items():
        print "MAIN KEY: %s" % mainkey
        print res.items()
        if mainkey == 'scan':
            for sub1k,sub1v in mainvalue.items():
                print "SUB1K: %s" % sub1k
                print "SUB1V: %s" % sub1v
###
# hold off on rev dns till i get threading working
###
#            ptr = getPTRvalue(sub1k)
                for sub2k,sub2v in sub1v.items():
                    print "sub2k: %s" % sub2k
                    print "sub2v: %s" % sub2v
                    if sub2k == 'tcp':
                        for k,v in sub2v.items():
                            if v['state'] == 'open':
                                #print "%s - %s" % (k,v['name'])
                                jsondata = {}
                                jsondata['ip'] = sub1k
                                jsondata['timestamp'] = str(datetime.datetime.now())
                                jsondata['ports'] = {}
                                socket.setdefaulttimeout(5)
#                                jsondata['reverse-dns'] = rec
      
                                for k,v in sub2v.items():
                                    if v['state'] == 'open':
                                        jsondata['ports'].update({k:v['name']})
                                with open(sub1k +'.json', mode ='w') as f:
                                    json.dump(jsondata,f, sort_keys=True)


#### No threading
#for host in hosts:
#    runScan(host)
####

## Threading logic borrowed and changed from:
## http://www.ibm.com/developerworks/aix/library/au-threadingpython/
##

queue = Queue.Queue()
          
class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
          
    def run(self):
        while True:
        #grabs host from queue
            host = self.queue.get()
            runScan(host) 
            
         #signals to queue job is done
            self.queue.task_done()
          
start = time.time()

def main():
       
   #spawn a pool of threads, and pass them queue instance 
    for i in range(threadCount):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
              
    #populate queue with data   

    for host in nm.listscan(hosts):
        print "HOST: ", host
        queue.put(host)
           
      #wait on the queue until everything has been processed     
    queue.join()
         
main()
print "Elapsed Time: %s" % (time.time() - start)
