#!/usr/bin/env python
'''
ToDo: extend script to connect to MySQL and
      run show tables?
'''

dbname  = 'testDB'
infile  = 'test.txt'

''' Sample input file - show tables;
| adobe_payloads                                       |
| app_lock_assignments                                 |
| application_usage_logs                               |
...etc
'''

outfile = '%s_DropTables.txt'%(dbname)

''' Sample output file
DROP TABLE IF EXISTS adobe_payloads;
DROP TABLE IF EXISTS app_lock_assignments;
DROP TABLE IF EXISTS application_usage_logs;
'''

readInFile     =  open(infile, 'r')
writeOutFile   =  open(outfile, 'w')
sqlcmd         = 'DROP TABLE IF EXISTS '

writeOutFile.write('use %s;\n'%(dbname))

for line in readInFile:
    finalOutput = sqlcmd + line.split('|')[1].strip()
    print finalOutput
    writeOutFile.write(finalOutput + ';\n')

readInFile.close()
writeOutFile.close()
