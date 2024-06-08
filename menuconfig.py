from typing import Any
from source import *
import sys,os



def __fu__(_o: list, _to: int, _with: Any):
    new_o = _o
    if len(_o) >= _to:
        return new_o
    while len(new_o) < _to:
        new_o.append(_with)
    return new_o


FILE: list[str] = open(Spin,"r").read().split("\n")


TermSize = (os.get_terminal_size().columns,os.get_terminal_size().lines)
ValidInputModes = [
    ["command",Fore.LIGHTBLUE_EX + ">"],
    ["write",Fore.GREEN + ":"]
]


def main():
    global FILE
    InputMode = ValidInputModes[0]
    KUFJBTCM = ">"
    cursor = 0
    lineTaken = 0
    while 1:
        #clearing the screen
        system("cls || clear")
        #runtime variables
        TermSize = (os.get_terminal_size().columns,os.get_terminal_size().lines)
        lineTaken = 0
        #text processing
        #text DrawLoop
        print(Fore.YELLOW + "-"*TermSize[0] + Style.RESET_ALL)
        lineTaken += 1
        for ln, text in enumerate(FILE):
            print((Fore.BLUE + "* " if cursor == ln else "  ") + Fore.YELLOW + str(ln) + "|" + (Fore.CYAN if cursor == ln else Fore.WHITE) + text + Style.RESET_ALL)
            lineTaken += 1
        print(f"   {Fore.YELLOW}|{Fore.BLUE + "~" + Style.RESET_ALL}\n"*(TermSize[1]-lineTaken-2),end="")
        print(Fore.YELLOW + "-"*TermSize[0] + Style.RESET_ALL)
        lineTaken += 1
        #input
        inp = input(InputMode[1]+" "+Fore.CYAN)
        if InputMode[0] == "command":
            match inp.split():
                case ["save"] | ["s"]:
                    with open(Spin,"w") as output:
                        for line in FILE:
                            output.write(line + "\n")
                        output.close()
                case ["SetCursor",ln] | ["sc",ln]:
                    cursor = int(ln)
                case ["rml", ln] | ["RemoveLine", ln]:
                    del FILE[int(ln)]
                case ["q"] | ["quit"]:
                    exit()
                case ["reload"] | ["r"]:
                    FILE = open(Spin,"r").read().split("\n")
                case ["write"] | ["w"]:
                    InputMode = ValidInputModes[1]
                case _:
                    print(Fore.RED + "command not found" + Style.RESET_ALL)
        elif InputMode[0] == "write":
            if inp == KUFJBTCM:
                InputMode = ValidInputModes[0]
            else:
                __fu__(FILE,cursor+2,"")
                FILE[cursor] = inp
                cursor += 1




try:
    main()
    #restoring the pressed keys
    os.system("cls||clear")
    #
except KeyboardInterrupt:
    #restoring the pressed keys
    os.system("cls||clear")
    #
    exit()
except Exception as err:
    print(err)
