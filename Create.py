import sys,os
from source import *

t = GetType(sys.argv[1])
target = sys.argv[-1]
if t == -1:
    print("Oops!. type is wrong.")

if t == OBJT_DIR:
    os.mkdir(target)
elif t == STRUCTURE:
    struct(target,"NULL")
elif t == OBJT_FILE:
    with open(target,"w") as f:
        f.close()
else:
    exit(-1)





