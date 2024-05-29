from os import system,path,listdir,getcwd
from json import loads as JsonLoad
from colorama import *
from tomllib import loads as TomlLoad

parent_dir = path.dirname(path.realpath(__file__))

OBJT_DIR = "directory"
OBJT_FILE = "file"

def GetType(Type: str) -> str|int:
    if Type[0] != "#":
        return -1
    match Type[1:]:
        case "dir":
            return OBJT_DIR
        case "file":
            return OBJT_FILE
        case _:
            return -1

def ListToString(_list: list[str]) -> str:
    string = ""
    for i in _list:
        string += i + " "
    return string

def RunCommand(command,args):
    system(f"{command} {ListToString(args)}")

if ".spin" in listdir(getcwd()):
    IsSpin = True
else:
    IsSpin = False
if IsSpin == True:
    with open(".spin") as f:
        config = JsonLoad(f.read())
else:
    with open(path.join(parent_dir,"UseConfig")) as d:
        ConfigPath = TomlLoad(d.read())["active"]
    with open(ConfigPath) as f:
        config = JsonLoad(f.read())
