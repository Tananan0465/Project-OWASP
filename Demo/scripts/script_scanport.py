from subprocess import PIPE, run
import os

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE,
                 universal_newlines=True, shell=True)
    return result.stdout


#nmap
def scanport(ip):
    fullPort = out("nmap -A -sV -iL " + ip + " -oG output.grep") #removed -p- arg for faster testing
    if os.path.exists("./results/portList.txt"):
        os.remove("./results/portList.txt")
    a= out('./porttest.sh')
    count = 0
    ip = ""
    webaddr = ""
    for line in open("./results/portList.txt", "r"):
        if line != "END\n":
            if count == 0 :
                ip = line.rstrip()
                count = count+1
            else:
                add = ip+":"+line
                webaddr = webaddr+ add
        else:
            count = 0
    outfile = open("./results/portList.txt", "w")
    outfile.write(webaddr)
    outfile.close()
    print("Port scan Completed")
    print("------------------------------")
