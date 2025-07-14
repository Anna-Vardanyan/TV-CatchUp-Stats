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
 
year=sys.argv[1]
month=sys.argv[2]
day_start=sys.argv[3]
day_end=sys.argv[4]

days=list(range(int(day_start),(int(day_end))+1))
print(days)

susername = "example_username"
spassword = "example_password"
ifname=[]
ofname=[]
ips=[]

for i in range(211,224):
#   print (i)
   ips.append('10.100.96.'+str(i))

ips.append('10.100.96.51')
ips.append('10.100.96.53')
ips.append('10.100.96.55')
ips.append('10.100.96.56')
#ips.append('10.100.96.16')

#print(ips)

oscmd=subprocess.Popen('mkdir -p ' + year + month + ' && ' + 'cd ' + year + month, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, error=oscmd.communicate()

for i in range(1,len(ips)+1):

#    oscmd2='mkdir -p '+ year + month + '/' + 'cups' + str(i).zfill(2)
#    bp=subprocess.Popen(oscmd2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#    output, error=bp.communicate()

    host = ips[i-1]
    print(host)
    for j in range(0,len(days)):
       origin = '/home/prod/cups/log/cups_stats.log-'+year+month+str(days[j]).zfill(2)+'.gz'
       destin = '/home/avardanyan/CUP_Stats/'+year+month+'/cups'+str(i).zfill(2)+'_stats.log-'+year+month+str(days[j]).zfill(2)+'.gz'
       print(origin)
       print(destin)
       os_scp=subprocess.Popen('sshpass -p' + spassword + ' scp -r ' + susername+'@'+host+':'+origin + ' ' +destin + ' && gunzip ' + destin, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
       output, error=os_scp.communicate()
       print(output)


#for k in range(1,len(days)+1):
for k in range(int(day_start),len(days)+1+int(day_start)-1):
    ofname.append('all_cups_stats.log-'+year+month+str(k).zfill(2))
    for l in range(1,len(ips)+1):
        ifname.append('cups'+str(l).zfill(2)+'_stats.log-'+year+month+str(k).zfill(2))
#       print(ifname[l-1])
#    print(ofname[k-1])
    print(ofname[k-int(day_start)])
    with open('/home/avardanyan/CUP_Stats/'+year+month+'/'+ofname[k-int(day_start)], 'w') as outfile:
        print(outfile)
        for m in range(0+(k-int(day_start))*(len(ips)),(k-int(day_start)+1)*len(ips)):
            print(ifname[m])
            with open('/home/avardanyan/CUP_Stats/'+year+month+'/'+ifname[m]) as infile:
                outfile.write(infile.read())

                