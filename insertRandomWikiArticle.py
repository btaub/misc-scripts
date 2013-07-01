#!/usr/bin/python

'''
A script to help get me familiar with pumping data into MySQL
'''

import urllib2 , httplib , socket
import MySQLdb

HOST = 'en.wikipedia.org'
URI  = '/wiki/Special:Random'
VERB = 'GET'
REPS =  1

'''
DB update example grabbed and changed a bit from:
    http://www.tutorialspoint.com/python/python_database_access.htm
'''
def insertIntoDB(the_title,the_output):
    # Open database connection
    db = MySQLdb.connect("localhost","testuser","testuser1","test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database. # Below works
    sql = """INSERT INTO tbl_test(col_title, col_output)
             VALUES(""" + "'" + db.escape_string(str(the_title)) + "'" + "," + "'" + db.escape_string(str(the_output)) + "'" + """)"""
    try:
       # Execute the SQL command
       cursor.execute(str(sql))

       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # disconnect from server
    db.close()

'''
    wikipedia.org redirects Special:Random to, well a random article
'''

def getRedirect():

    socket.setdefaulttimeout(20)

    try:
        conn = httplib.HTTPConnection(HOST, 80)
        conn.set_debuglevel(0)
        conn.request(VERB , URI)
        r1 = conn.getresponse()
        data = r1.read()
        conn.close()

        if r1.status == 302 or r1.status == 301:
            url = r1.msg['Location']
            return url

    except:
        print "Could not connect to " + URI 

'''
    Read the article into a string
'''
def getArticle(article):
    req        = urllib2.Request(article)
 #   req.add_header('Host'       , HOST)
    req.add_header('User-Agent' , 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:21.0) Gecko/20100101 Firefox/21.0')
    response   = urllib2.urlopen(req)
    the_title  = article
    the_output = response.read()
    return urllib2.unquote(the_title),urllib2.unquote(the_output)

for each in range(REPS):
    print each
    theUrl     = getRedirect()
    theArticle = getArticle(theUrl)
    tryit      = insertIntoDB(str(theArticle[0]), str(theArticle[1]))
