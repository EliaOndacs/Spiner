import sys,shutil,os
from source import *

def Oops(func, path, exc_info):
    print("something gone wrong")
    exit(-1)





t = GetType(sys.argv[1])
target = sys.argv[-1]
if t == -1:
    print("Oops!. type is wrong.")

if t == OBJT_DIR:
    shutil.rmtree(sys.argv[-1],onerror=Oops)
elif t == OBJT_FILE:
    os.remove(target)
else:
    exit(-1)
