import os


def genDirName(name):
    folderName = str(name)
    return folderName

def genDir():
    dirname = open("./temp/url_temp.txt", "r").read()
    if os.path.exists(f"./results/{genDirName(dirname)}"):
        return
    os.mkdir(f"./results/{genDirName(dirname)}")
    # try:
    #     os.mkdir(f"./results/{genDirName(dirname)}")
    #     print("result folder created.\n")
    # except OSError as error:
    #     print("result folder is already exist\n")
    #     return
