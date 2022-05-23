from subprocess import PIPE, run
import os
import json
from scripts.genDir import genDirName

def hsts():
    dirname = open("./temp/url_temp.txt", "r").read()
    hstsResult = open(f"./results/{genDirName(dirname)}/hstsResult.txt", "w")
    temp = open("url.txt", "r").read()
    os.system("curl -s -D- " + temp + " | grep -i strict > ./temp/hsts_read.txt")
    temp = open("./temp/hsts_read.txt", "r").read()
    hststemp = open("./temp/hsts_temp.txt", "w")
    if "strict-transport-security" not in temp and "Strict-Transport-Security" not in temp :
        data = open("./temp/ssl.json", "r").read()
        temp = json.loads(data)[0]
        hststemp.write(str(temp["endpoints"][0]["details"]["hstsPolicy"]))
        hststemp.close()
        hststemp = open("./temp/hsts_temp.txt", "r").read()
        if "present" not in hststemp:
            hstsResult.write("HSTS not supported")
            hstsResult.close()
            print("hsts process: No HSTS")
            return
    hstsResult.write("You have Strict Transport Security (HSTS).\n")
    hstsResult.close()
    print("hsts process: completed")


def ssl(url):
    temp = open(url, "r").read()
    os.system("go run ./tools/ssllabs/ssllabs-scan-v3.go "+ temp +" > ./temp/ssl.json")
    tls()
    hsts()
    print("SSL Completed")
    print("------------------------------")



def tls():
    data = open("./temp/ssl.json", "r").read()
    temp = json.loads(data)[0]
    dirname = open("./temp/url_temp.txt", "r").read()
    tlsResult = open(f"./results/{genDirName(dirname)}/tlsResult.txt", "w")
    for i in temp["endpoints"][0]["details"]["protocols"]:
        tlsResult.write(str(i)+"\n")
    tlsResult.close()
    print("tls process: completed")
