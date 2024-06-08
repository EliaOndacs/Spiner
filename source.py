from os import system,path,listdir,getcwd
from json import loads as JsonLoad
from colorama import *
from tomllib import loads as TomlLoad
import keyboard

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

def getc():
    try:
        return keyboard.read_key()
    except KeyboardInterrupt:
        return None

def RunCommand(command,args):
    system(f"{command} {ListToString(args)}")

with open(path.join(parent_dir,"UseConfig")) as d:
    ConfigPath = TomlLoad(d.read())["active"]

if ".spin" in listdir(getcwd()):
    IsSpin = True
    Spin = path.join(getcwd(),".spin")
else:
    IsSpin = False
    Spin = ConfigPath
if IsSpin == True:
    with open(".spin") as f:
        config = JsonLoad(f.read())
else:
    with open(ConfigPath) as f:
        config = JsonLoad(f.read())
