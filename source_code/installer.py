import requests
import os
import ctypes, sys

def Installer():
    # install dir
    InstallDir = os.getenv("APPDATA") + "\\computer-outro\\"
    try: 
        os.mkdir(InstallDir) 
    except OSError as error: 
        pass 

    # URL
    outroURL = "https://github.com/DecodedFinn/computer-outro/raw/main/outro.mp3"
    exeURL = "https://github.com/DecodedFinn/computer-outro/raw/main/computer-outro.exe"

    print("Downloading the outro.mp3 file...")
    response = requests.get(outroURL)
    open(f"{InstallDir}outro.mp3", "wb").write(response.content)
    print("Download complete.")

    print("Please pick one.")
    choice = input("There are 2 options. \n Option 1: bsod \n Option 2: Shutdown \n> ")

    if choice == "1":
        print("Configuring computer-outro to use bsod")
        open(f"{InstallDir}bsod", "wb")
        print("Success!")

    elif choice == "2":
        print("Configuring computer-outro to use Shutdown")
        open(f"{InstallDir}shutdown", "wb")
        print("Success!")
    else:
        print("Invalid aborting.....")
        
    choice1 = input("Do you want to make the shutdown button run the outro? (y/n) ")

    if choice1 == "y":
        print("Okay Downloading and Installing...")
        response = requests.get(exeURL)
        open(f"C:\\WINDOWS\\System32\\GroupPolicy\\Machine\\Scripts\\Shutdown\\computer-outro.exe", "wb").write(response.content)
        print("Done now you can try it out")
    elif choice1 == "n":
        print("Okay where do you want to Download the computer-outro?")
        path = input("Path: ")
        response = requests.get(exeURL)
        open(f"{path}\\computer-outro.exe", "wb").write(response.content)
        print(f"Done now you can try to run it at: {path}")
    else:
        print("Invalid input")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    Installer()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
