from subprocess import PIPE, run
import tldextract
import os
import time

#nmap
fullPort = out("nmap -A -sV -iL dnsNoDup.txt -oG output.grep") #removed -p- arg for faster testing
if os.path.exists("portList.txt"):
  os.remove("portList.txt")
a= out('./porttest.sh')
count = 0
ip = ""
webaddr = ""
for line in open("portList.txt", "r"):
    if line != "END\n":
        if count == 0 :
            ip = line.rstrip()
            count = count+1
        else:
            add = ip+":"+line
            webaddr = webaddr+ add
    else:
        count = 0
outfile = open("portList.txt", "w")
outfile.write(webaddr)
outfile.close()