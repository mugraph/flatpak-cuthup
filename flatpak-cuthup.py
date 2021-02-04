#!/usr/bin/python3

### Flatpak Custom Theme Updater
### SOURCE: https://github.com/hkdb/gnome-ftu
### SCRIPT: flatpak-cuthup.py
### DESCRIPTION: Automated custom theme update for Flatpak Apps

import os, datetime, sys, glob, shutil, string
from pathlib import Path

# Define Version
version = "v00.01"

# Get HomeDir
homedir = str(Path.home())

# Get current theme being used
print("\nIdentifying which theme is currently being used...")
theme = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
theme = theme[1:-2]
print("THEME: " + theme)

# Check what theme folders in flatpak exists
print("\nChecking Flatpak Gnome Platform Dependencies...")
gnome_platforms = os.listdir(homedir + "/.local/share/flatpak/runtime/org.gnome.Platform/x86_64/")
for p in gnome_platforms:
    print("Gnome " + p)

#Check for freedesktop folders as well
print("\nChecking Flatpak Freedesktop Platform Dependencies...")
free_platforms = os.listdir(homedir + "/.local/share/flatpak/runtime/org.freedesktop.Platform/x86_64/")
for p in free_platforms:
    print("Freedesktop " + p)

# Check on where theme exists
orig = ""
print("\nChecking to see where the theme dir is...")
home = os.path.isdir(homedir+"/.local/share/themes/"+theme)
print("HOME: ", home)
if home == True:
    orig = homedir+"/.local/share/themes/"+theme
else:
    system = os.path.isdir("/usr/share/themes/"+theme)
    print("SYSTEM: ", system)
    if system == True:
        orig = "/usr/share/themes/"+theme
    else:
        print("ERROR: No such theme available in the 2 common places to find them. Please move your theme folder to either ~/.local/share/themes/ or /usr/share/themes/ and try again.\n")
        exit()

# copy theme over to all available platforms
print("\nCopying theme to all available platforms...")
for p in gnome_platforms:
    print("COPYING TO: Gnome",  p)
    os.system("cp -R " + orig + " " + homedir + "/.local/share/flatpak/runtime/org.gnome.Platform/x86_64/" + p + "/active/files/share/themes/")
for p in free_platforms:
    print("COPYING TO: Freedesktop",  p)
    os.system("cp -R " + orig + " " + homedir + "/.local/share/flatpak/runtime/org.freedesktop.Platform/x86_64/" + p + "/active/files/share/themes/")

print("\nDONE...\n")
