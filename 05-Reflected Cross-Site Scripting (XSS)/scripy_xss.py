from subprocess import PIPE, run
import os
import time
import subprocess

def XSS():
    XSSResult = open("XSSResult.txt", "w")
    for line in open("dnsNoDup.txt", "r"):
        subprocess1 = subprocess.Popen("python xsssniper.py -u '"+line+"' --crawl --forms", shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocess1.stdout.read()
        #print(subprocess_return)
        XSSResult.write(subprocess_return.decode("utf-8"))
    XSSResult.close()



XSS()
