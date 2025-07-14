#!/usr/bin/python3

import sys
import os
import subprocess
import numpy
import shlex
import io
import string
import array
import paramiko
 
#year=sys.argv[1]
#month=sys.argv[2]
#day_start=sys.argv[3]
#day_end=sys.argv[4]

#days=list(range(int(day_start),(int(day_end))+1))
#print(days)

susername = "example_username"
spassword = "example_password"
ips=[]

for i in range(211,224):
#   print (i)
   ips.append('10.100.96.'+str(i))

ips.append('10.100.96.51')
ips.append('10.100.96.53')
ips.append('10.100.96.55')
#ips.append('10.100.96.56')
#print(ips)

#for j in range(0,len(days)):
for j in range(0,1):
    origin = '/home/prod/cups/log/cups_stats.log-20171221'
    destin = '/home/prod/cups/log/cups_stats.log-2021'
    ndestin1 = '/home/prod/cups/log/cups_stats.log-20171220'
    ndestin2 = '/home/prod/cups/log/cups_stats.log-20171221'
#    print(origin)
#    print(destin)

    for i in range(1,len(ips)+1):
        host = ips[i-1]
        print(host)
#        rcmd1 = 'sshpass -p' + spassword + ' ssh ' + susername+'@'+host + ' ' +'mv ' + origin + ' ' + destin
        rcmd2 = 'sshpass -p' + spassword + ' ssh ' + susername+'@'+host + ' \"' + ' cat ' + destin + ' |grep \'2017-12-20 \' > ' + ndestin1 + ' ; ' + 'gzip ' + ndestin1 + '\"'
        rcmd3 = 'sshpass -p' + spassword + ' ssh ' + susername+'@'+host + ' \"' + ' cat ' + destin + ' |grep \'2017-12-21 \' > ' + ndestin2 + '\"'
        print(rcmd2)
#        os_cmd1=subprocess.Popen(rcmd1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#        output1, error1=os_cmd1.communicate()
#        print(output1)
        os_cmd2=subprocess.Popen(rcmd2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output2, error2=os_cmd2.communicate()
        print(output2)
        os_cmd3=subprocess.Popen(rcmd3, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output3, error3=os_cmd3.communicate()
        print(output3)

