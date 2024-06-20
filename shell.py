from source import *
import sys,os,shutil
import requests

def OneLine(line: str):
    match line.split(" "):
        case ["exit"]:
            exit()
        case ["cd",path]:
            os.chdir(path)
        case ["list"]:
            print(os.listdir(os.getcwd()))
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
        case ["Pkg",do,*commands]:
            match do:
                case "install":
                    RunCommand(config["Pkg"]["Install"],list(commands))
                case "uninstall":
                    RunCommand(config["Pkg"]["Uninstall"],list(commands))
                case "all":
                    RunCommand(config["Pkg"]["All"],list(commands))
                case "fetch":
                    response = requests.get(list(commands)[1])
                    if response.status_code == 200:
                        with open(list(commands)[0], 'wb') as f: # type: ignore
                            f.write(response.content) # type: ignore
                        print(Fore.GREEN + 'Content downloaded successfully!' + Style.RESET_ALL)
                    else:
                        print(Fore.RED + 'Failed to download the Content.' + Style.RESET_ALL)

def RunFromFile(path: str):
    if not path.endswith(".sph"):
        print(Fore.RED + "Invalid file extension. Only .sph files are supported." + Style.RESET_ALL)
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


