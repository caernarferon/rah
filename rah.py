import os
import requests
import subprocess
import argparse
parse = argparse.ArgumentParser()
parse.add_argument('-i', '--install', nargs='?', const=True, help='install a package duh')
parse.add_argument('-r', '--remove', nargs='?', const=True, help='remove a package duh')
args = parse.parse_args()

class Rah:
    def __init__(self):
        self.version = 0.1
        self.rahdir = os.path.expanduser("~/.rah")

    def checkmkdir(self):
        if not os.path.isdir(self.rahdir):
            print("you dont have a rah directory, creating one...")
            os.mkdir(self.rahdir)
        else:
            return("rah directory located, moving on")
    def install(self, packageName):
        subprocess.run(["git", "clone", f"https://aur.archlinux.org/{packageName}.git"])
        os.chdir(self.package)
        os.system("makepkg -sri")

rah = Rah() #capitalization
rah.checkmkdir()

package_name = input("what are you installing today: ")
rah.install(package_name)