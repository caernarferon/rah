#!/usr/bin/env python3

import argparse
import requests
import os
import subprocess

def search_aur(package_name):
    Furl = 'https://aur.archlinux.org/rpc/?v=5&type=search&arg=' + package_name
    rq = requests.get(Furl)
    rqj = rq.json()
    if rqj['results']:
        results = rqj['results']
        sorted_results = sorted(results, key=lambda r: r['NumVotes'], reverse=True)
        print(f"\ni found {len(results)} results for '{package_name}':\n")
        for i in range(min(5, len(sorted_results))):
            result = sorted_results[i]
            print(f"{i + 1}. {result['Name']}, with {result['NumVotes']} upvotes. description: {result['Description']}\n")
        selected = input('which one do you want (put a number in duh) ')
        if selected == '':
            exit()
        try:
            selected = int(selected) - 1
            result = sorted_results[selected]
            url = result['PackageBase']
            try:
                os.chdir('/opt/rok/')
            except FileNotFoundError:
                print("rok directory not found, creating one...")
                os.system("sudo mkdir /opt/rok")
            except OSError:
                print("this isnt supposed to happen")
            result = subprocess.run(['sudo', 'git', 'clone', f'https://aur.archlinux.org/{url}.git'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(url)
                os.chdir(url)
                os.system('makepkg -sri')
        except (requests.exceptions.RequestException, ValueError, IndexError) as error:
            print(f"oh boy something messed up.{error}")
            return

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='my little aur helper')
    parser.add_argument('package_name', metavar='PKG_NAME', type=str, nargs='?',
                        help='the name of the package to install')
    args = parser.parse_args()

    if args.package_name:
        search_aur(args.package_name)
    else:
        package_name = input('hi what are you looking for? ')
        search_aur(package_name)
