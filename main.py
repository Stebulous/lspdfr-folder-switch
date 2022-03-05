import os
from time import sleep
from tkinter import Tk, filedialog

print(r'GTA Folder Switcher v0.1')

root = Tk()
root.withdraw()

chosendir = filedialog.askdirectory(parent=root,initialdir="/",title='Please select your Steam Library common directory')

try:
    current_dir = os.path.join(chosendir, r"Grand Theft Auto V")
    clean_dir = os.path.join(chosendir, "GTAV - Clean")
    lspdfr_dir = os.path.join(chosendir, "GTAV - LSPDFR")
    
    if not (os.path.exists(clean_dir) or os.path.exists(lspdfr_dir)):
        if not (os.path.exists("Grand Theft Auto V")):
            raise NotADirectoryError("Failed to find any GTA directory!")
    
    print("Searching Current Directory...\n")
    os.chdir(current_dir)
    
    if (os.path.exists(os.path.join(current_dir, "mods"))):


        if (os.path.exists(os.path.join(current_dir, "lspdfr"))):
            print('Current direcory is the LSPDFR directory.')
            sleep(1)
            print("\nSwitching Folders to Clean Version...\n")
            os.chdir(chosendir)
            os.system(r'ren "Grand Theft Auto V" "GTAV - LSPDFR')
            os.system(r'ren "GTAV - Clean" "Grand Theft Auto V')
        else:
            print('Current Directory Is Modded.')
            sleep(1)
            print("\nSwitching Folders to Clean Version...\n")
            os.chdir(chosendir)
            os.system(r'ren "Grand Theft Auto V" "GTAV - Modded')
            os.system(r'ren "GTAV - Clean" "Grand Theft Auto V')
    else:
        print('Current directory is the Clean directory.')
        sleep(1)
        print("\nSwitching Folders...\n")
        os.chdir(chosendir)
        os.system(r'ren "Grand Theft Auto V" "GTAV - Clean')
        os.system(r'ren "GTAV - LSPDFR" "Grand Theft Auto V')
   
  
    print("\n\n All done!")
    sleep(5)
except Exception as err:
    print(err)
    sleep(5)
    quit(1)
