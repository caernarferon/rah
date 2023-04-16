#!/usr/bin/env python3

import os
try:
    os.system("sudo cp rock.py ~/.local/share/rah/scripts")

except (NotADirectoryError):
    print("did you install caveman linux yet?")
    os.system("sudo mkdir ~/.local/share/rah")
    os.system("sudo mkdir /.local/share/rah/scripts")
finally:
    os.system("sudo cp rock.py ~/.local/share/rah/scripts")
os.system("sudo touch rah /usr/local/bin")
os.system("sudo echo ")