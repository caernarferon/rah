#!/usr/bin/env python3

import os
try:
    os.system("sudo cp rock.py /opt/rok/scripts")

except (NotADirectoryError):
    print("did you install caveman linux yet?")
    os.system("sudo mkdir /opt/rock/")
    os.system("sudo mkdir /opt/rock/scripts")

os.system("sudo touch /usr/local/bin")
os.system("sudo echo ")