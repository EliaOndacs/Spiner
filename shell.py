from source import *
import sys,os,shutil


def OneLine(line: str):
    match line.split(" "):
        case ["exit"]:
            exit()
        case ["Create",type,path]:
            t = GetType(type)
            target = path
            if t == -1:
                print("Oops!. type is wrong.")

            if t == OBJT_DIR:
                os.mkdir(target)
            elif t == OBJT_FILE:
                with open(target,"w") as f:
                    f.close()
            else:
                exit(-1)
        case ["Remove",type,path]:
            def Oops(func, path, exc_info):
                print("something gone wrong")
                exit(-1)
            t = GetType(type)
            target = path
            if t == -1:
                print("Oops!. type is wrong.")

            if t == OBJT_DIR:
                shutil.rmtree(path,onerror=Oops)
            elif t == OBJT_FILE:
                os.remove(target)
            else:
                exit(-1)
        case ["Pkg",*commands]:
            RunCommand(config["DefaultPkg"],list(commands))

def RunFromFile(path: str):
    if not path.endswith(".SpinSh"):
        print(Fore.RED + "Invalid file extension. Only .SpinSh files are supported." + Style.RESET_ALL)
        exit(-1)
    with open(path) as f:
        program = (f.read()).split("\n")
    for line in program:
        OneLine(line)

if len(sys.argv) > 1:
    RunFromFile(sys.argv[-1])
else:
    while 1:
        command = input(Back.WHITE + Fore.BLACK + "$>" + Style.RESET_ALL + " ")
        OneLine(command)


