#!/usr/bin/env python3

import os

try:
    os.system("sudo cp rah.py ~/.local/share/rah/scripts/rah")
except NotADirectoryError:
    print("Did you install Caveman Linux yet?")
    os.system("sudo mkdir -p ~/.local/share/rah/scripts")
    os.system("sudo cp rah.py ~/.local/share/rah/scripts/rah")
finally:
    os.system("sudo ln -s ~/.local/share/rah/scripts/rah ~/.local/share/rah/scripts/rah.py")

# Create a symbolic link to the script in /usr/local/bin
os.system("sudo ln -s ~/.local/share/rah/scripts/rah.py /usr/local/bin/rah")
