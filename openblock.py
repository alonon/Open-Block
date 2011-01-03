import os.path
#!/usr/bin/python
# OnurAKTAS.net - ALonon.net - acikfikir.org
# Nov 27, 2010 11:07:11 PM
# OpenBlock v1.0
import subprocess
import sys
import re
import urllib2
import os

#Host File
hostFile = '/etc/hosts'

if(len(sys.argv) != 2):
    print "Usage:sudo python openblock.py domainname.com"
else:
    domainName = sys.argv[1].replace("http://",'',1)
    domainName = sys.argv[1].replace("www.",'',1)
    try:
        openWebsite = urllib2.urlopen('http://domaintoip.com/ip.php?domain='+domainName)
    except:
         print "Can not get ip address of",domainName
    result_str = openWebsite.read()
    result_str = re.findall('[0-9]+(?:\.[0-9]+){3}',result_str)
    try:
        if result_str[0] != "":
            try:
                if not os.path.isfile(hostFile):
                    print "You have to change your hosts file in openblock.py line: 13"
                    sys._exit(0)
                else:
                    openFile = open ( hostFile, 'a+' )
                    openFile.write ("\n"+result_str[0]+' '+domainName)
                    openFile.write ("\n"+result_str[0]+' www.'+domainName)
                    print("Writed in /etc/hosts\n")
                    openFile.close()
                    restart = 1
            except:
                print "run with 'sudo' sudo python openblock domainname.com"
                restart = 0
            if restart:
                try:
                    print "restarting network ...\n"
                    process = subprocess.Popen("/etc/init.d/networking restart", shell=True)
                    process.wait()
                except:
                    print "network can not restarted !"
    except:
        print "Can not get ip address of",domainName," \nDid you run with 'sudo'? sudo python openblock domainname.com"