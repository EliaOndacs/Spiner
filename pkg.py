from source import *
import sys
import requests


match sys.argv[1]:
    case "install":
        RunCommand(config["Pkg"]["Install"],sys.argv[2:])
    case "uninstall":
        RunCommand(config["Pkg"]["Uninstall"],sys.argv[2:])
    case "all":
        RunCommand(config["Pkg"]["All"],sys.argv[2:])
    case "fetch":
        response = requests.get(sys.argv[1])
        if response.status_code == 200:
            with open(sys.argv[2], 'wb') as f: #type: ignore
                f.write(response.content) #type: ignore
            print(Fore.GREEN + 'Content downloaded successfully!' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Failed to download the Content.' + Style.RESET_ALL)

