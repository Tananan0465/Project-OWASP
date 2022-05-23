from subprocess import PIPE, run
import os
from scripts.grepfile import grepfile


def xss(hostname):
    temp = open(hostname, "r").read()
    os.system("sudo python3 ./tools/XSStrike/xsstrike.py -u \"" + temp + "\" --crawl > ./temp/crawl_temp.txt")
    grepfile("./temp/crawl_temp.txt")
    # isparam = input("Do you have parameter (Y/n): ")
    # isparam = isparam.lower()
    # if isparam == 'n' or isparam == 'no' :
    #     os.system("sudo python3 ./tools/XSStrike/xsstrike.py -u \"" + temp + "\" --crawl > ./temp/crawl_temp.txt")
    #     grepfile("./temp/crawl_temp.txt")
    #     return
    # elif isparam == 'y' or isparam == 'yes':
    #     os.system("sudo python3 ./tools/XSStrike/xsstrike.py -u \"" + temp + "\" --crawl > ./temp/xsstest.txt")
    #     return
    # else :
    #     xss(hostname)

# xss("../url.txt")

def setHost(url):
    urlread = open(url,"r").read()
    host = open("./temp/xssurl_temp.txt", "w")
    host.write("http://"+urlread)
    host.close()
    xss("./temp/xssurl_temp.txt")
    

def xssmain(url):
    setHost(url)
