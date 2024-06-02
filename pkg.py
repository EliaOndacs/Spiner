from source import *
import sys

match sys.argv[1]:
    case "install":
        RunCommand(config["Pkg"]["Install"],sys.argv[2:])
    case "uninstall":
        RunCommand(config["Pkg"]["Uninstall"],sys.argv[2:])
    case "all":
        RunCommand(config["Pkg"]["All"],sys.argv[2:])

