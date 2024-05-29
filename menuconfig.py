from source import *


def MenuConfig():
    #ActiveSetting
    if IsSpin == False:
        get = input("ActiveConfigPath [default: @GSC]: ")
        ActiveSetting = get if get != "" else (path.join(parent_dir,"Spiner_settings.json")).replace("\\","\\\\")
        #operating
        if path.isfile(ActiveSetting):
            with open(path.join(parent_dir,"UseConfig"),"w") as f:
                f.write(f"active = {'"'+ActiveSetting+'"'}")
                f.close()
        else:
            print(Fore.RED + f"the ActiveConfig file is not valid or is a directory.\ndetail: `{ActiveSetting}`" + Style.RESET_ALL)
            print(Fore.RED + "re-config please" + Style.RESET_ALL)
            MenuConfig()
    ###############################
    pass

if IsSpin == True:
    print(Fore.CYAN + ".spin found in the directory.\nconfig will be set from there." + Style.RESET_ALL)

MenuConfig()

