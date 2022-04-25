from subprocess import PIPE, run
import os
import time
import subprocess

def httpInsecure():
    httpInsecureResult = open("httpInsecureResult.txt", "w+")
    for line in open("dnsNoDup.txt", "r"):
        subprocess1 = subprocess.Popen("curl -s -D- " + line +"| grep -i Strict", shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocess1.stdout.read()
        #print(type(subprocess_return))
        httpInsecureResult.write(subprocess_return.decode("utf-8"))
    httpInsecureResult.close()



httpInsecure()