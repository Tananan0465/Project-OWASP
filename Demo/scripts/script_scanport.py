from subprocess import PIPE, run
import os
from scripts.genDir import genDirName

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout


#nmap
def scanport(ip):
    dirname = open("./temp/url_temp.txt", "r").read()
    fullPort = out("sudo nmap -A -sV -iL " + ip + " -oG output.grep") #removed -p- arg for faster testing
    if os.path.exists(f"./results/{genDirName(dirname)}/portList.txt"):
        os.remove(f"./results/{genDirName(dirname)}/portList.txt")
    a= out('./porttest.sh')
    count = 0
    ip = ""
    webaddr = ""
    for line in open(f"./temp/portList_temp.txt", "r"):
        if line != "END\n":
            if count == 0 :
                ip = line.rstrip()
                count = count+1
            else:
                add = ip+":"+line
                webaddr = webaddr+ add
        else:
            count = 0
    outfile = open(f"./results/{genDirName(dirname)}/portList.txt", "w")
    outfile.write(webaddr)
    outfile.close()
    print("Port scan Completed")
    print("------------------------------")
