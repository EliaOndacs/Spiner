from source import *
import sys
import pickle

if len(sys.argv) != 2:
    print(Fore.YELLOW + "usage: run [filename.pkl]") # type: ignore
    exit(1)

if sys.argv[-1].endswith(".pkl"):
    filename = sys.argv[-1]
else:
    print(Fore.RED+ f"Expected .pkl File. Found `.{sys.argv[-1].split(".")[-1]}` !") # type: ignore
    exit(1)


target_folder = folder([],"")
with open(filename,"rb") as target:
   data = pickle.load(target)

target_folder.SetDict(data)


Generate(target_folder)


