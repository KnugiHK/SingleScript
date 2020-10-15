from winreg import *
import ctypes, os

is_windows = (False if os.name != 'nt' else True) #Check if program is running on Windows

if is_windows:
    try:  
        #Check if program is running with admin privileges
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print("You need to run this program with admin privileges!")
        exit(0)

    #Set the path of target key
    parent = "Directory\\Background\\shell"
    noadmin = parent + "\\qcmd"
    admin = parent + "\\runas"
    exist = False
    try:
        reg = ConnectRegistry(None, HKEY_CLASSES_ROOT)
        k = OpenKey(reg, noadmin)
        l = OpenKey(reg, admin)
        exist = True
    except:
        pass

#Main Action
def install():
    if not exist:
        try:
            #Without Admin
            key = CreateKey(HKEY_CLASSES_ROOT, parent)
            SetValue(key, "qcmd", REG_SZ, "Open CMD here")
            key = CreateKey(HKEY_CLASSES_ROOT, noadmin)
            SetValue(key, "command", REG_SZ, "cmd.exe")
            registry_key = OpenKey(HKEY_CLASSES_ROOT, noadmin, 0, KEY_WRITE)
            SetValueEx(registry_key, "Icon", 0, REG_SZ, "imageres.dll,-5323")
            CloseKey(key)

            #With Admin
            key = CreateKey(HKEY_CLASSES_ROOT, parent)
            SetValue(key, "runas", REG_SZ, "Open CMD here(Admin)")
            key = CreateKey(HKEY_CLASSES_ROOT, admin)
            SetValue(key, "command", REG_SZ, "cmd.exe /s /k pushd \"%V\" & echo You are running Command Prompt under admin privileges.")
            registry_key = OpenKey(HKEY_CLASSES_ROOT, admin, 0, KEY_WRITE)
            SetValueEx(registry_key, "Icon", 0, REG_SZ, "imageres.dll,-5324")
            CloseKey(key)

            print("This function has been added to your computer.") 
        except:
            print("Error")
    else:
        print("This function already exist.")

def uninstall():
    if exist:
        try:
            DeleteKey(HKEY_CLASSES_ROOT, noadmin + "\\command")
            DeleteKey(HKEY_CLASSES_ROOT, noadmin )
            DeleteKey(HKEY_CLASSES_ROOT, admin + "\\command")
            DeleteKey(HKEY_CLASSES_ROOT, admin )
            print("This function has been removed from your computer.")
        except:
            print("Error")
    else:
        print("This function does not exist in your computer.")

#Main
if __name__ == '__main__' and is_windows:
    version = "v2"
    print("Open Command Prompt in Current Directory Installer (" + version + ")")
    action = input("Please select the action you want to perform: (A)Install (B)Uninstall" + "\n").upper()
    if action == "A":
        install()
    elif action == "B":
        uninstall()
    else:
        print("You can only type \"A\" or \"B\"")
