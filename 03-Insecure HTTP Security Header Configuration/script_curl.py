from subprocess import PIPE, run
import os
import time


def httpInsecure():
    i=1
    httpInsecureResult = open("httpInsecureResult.txt", "w")
    for line in open("portLists.txt", "r"):
        # print("curl -s -D- " + line + " | grep -i Strict")
        m = os.system("curl -s -D- " + line + " | grep -i Strict")
        i = i+1
        # httpInsecureResult.write()
    httpInsecureResult.close()



httpInsecure()