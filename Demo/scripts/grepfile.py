import os

def grepfile(file):
    r = open(file,"r")
    f = open("./temp/xss_crawl.txt", "w")
    for line in r:
        if "Potentially" in line or "Vulnerable webpage" in line:
            f.write(line)
    f.close()
    formatxss()
    print("XSS Completed")
    print("------------------------------")


def formatxss():
    r = open("./temp/xss_crawl.txt","r")
    f = open("./results/xss_crawl_formated.txt", "w")
    if os.stat("./temp/xss_crawl.txt").st_size == 0:
        f.write("Nothing")
        f.close()
        return
    for line in r:
        if "Potentially" in line:
            f.write(line[13:-6]+"\n")
        elif "Vulnerable webpage" in line:
            f.write(line[15:35])
            f.write(line[40:-10]+"\n")
    f.close()