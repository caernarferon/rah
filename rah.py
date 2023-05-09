import os
import requests
import subprocess
import argparse
parse = argparse.ArgumentParser()
parse.add_argument('-s', '--search', nargs='?', const=True, help='search for a package duh')
args = parse.parse_args()

class Rah:
    def __init__(self):
        package = package_name
        packagedata = 
        self.version = 0.1
        self.rahdir = os.path.expanduser("~/.rah")
        self.version = package
    def packageinfo(self, package_name):
        package = package_name
        self.version
    def isitrealtho(self, package_name):
        url = f"https://aur.archlinux.org/packages/{package_name}"
        response = requests.get(url)
        return response.status_code == 200
    def checkmkdir(self):
        if not os.path.isdir(self.rahdir):
            print("you dont have a rah directory, creating one...")
            os.mkdir(self.rahdir)
        else:
            return("rah directory located, moving on")
    def install(self, package_name):
        os.chdir(self.rahdir)
        print(f"changing to rah directory... {self.rahdir}")
        try:
            subprocess.run(["git", "clone", f"https://aur.archlinux.org/{package_name}.git"])
        except subprocess.CalledProcessError as e:
            if "already exists" in str(e):
                print("i think that directory already exists. deleting...")
            else:
                print("uh oh: ", e)
        os.chdir(package_name)
        os.system("makepkg -sri")

rah = Rah() #capitalization
rah.checkmkdir()

package_name = input("what are you installing today?: ")
rah.install(package_name)