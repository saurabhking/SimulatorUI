import csv
import paramiko
import subprocess
import ConfigParser
import socket
import ConfigParser

def read_config_file(conf_file):
         try:
            config=ConfigParser.ConfigParser()
            with open(conf_file,'r') as conf_file:
                config.readfp(conf_file)
            return config
         except Exception as e:
            print e
conf=read_config_file('files.cfg')
         #print "End of config file"



import os
currd = os.getcwd()
print currd
myfile = open(currd + "/../healthchk/Filesystem_Checks.csv", 'wb')
wr = csv.writer(myfile)
header = ["FileSystem Checks Integration"]
healthchklist = []
healthchklist.append("FileChecks Integration")
#wr.writerow(header)
#wr.writerow(healthchklist)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ip  = open("ping_int.txt","r")
#data = ip.readlines()
#data = read_config_file.conf
try:
    rwlist = []
    rolist = []
    for line in conf.options('integration'):
     IP_details=conf.get('integration',line)
     data=IP_details.strip("\n")
     #print data
     #ips = ips.strip("\n")
     #print ips
     #ssh.connect(ips,username='ushukla',password='nu@2017',timeout=10)
     ssh.connect(data,username='root',password='Charter1',timeout=10)
     #ssh.connect(ips,timeout=10)
     chan = ssh.get_transport().open_session()
     chan.get_pty()
     chan.exec_command("'grep' '\sro[\s,]' /proc/mounts -c")
     #chan.exec_command("ping -c 5 chfapps-ctec-a1p.enwd.co.ss.charterlab.com")
     result =  [chan.recv(1024)]
     #stdin, stdout, stderr = chan.exec_command("ping -c 5 chfapps-ctec-a1p.enwd.co.ss.charterlab.com"
     #result = result.strip("\r\n")
     #print result
     #print stdout
     if result == ['0\r\n']:
      print  data + " " + "is" + " " + "Read/Write Device"
      rwlist.append(data)
      #print rwlist
      #wr.writerow(healthchklist)
     else:
      print  data + " " + "is "+ " " +"ReadOnly Device"
      rolist.append(data)
      #print rolist
      #healthchklist.append(rolist)

    if not  rolist:
       print "PASS"
       #print rwlist
       healthchklist.append("PASS")
       #healthchklist.append(rwlist)
       wr.writerow(healthchklist)
    else:
         print "FAIL"
         print rolist
         healthchklist.append("FAIL")
         healthchklist.append('\n'.join(rolist))
         healthchklist.append(rolist)
         wr.writerow(healthchklist)     
##except socket.gaierror as e:
except Exception as e:
  print e
#if not rwlist:

