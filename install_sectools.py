#!/usr/bin/env python3

import subprocess
import os
import sys

# Apps to install
REPOS=["https://github.com/Wh04m1001/DFSCoerce.git",
       "https://github.com/lgandx/Responder.git",
       "https://github.com/cddmp/enum4linux-ng.git",
       "https://github.com/robertdavidgraham/masscan.git",
       "https://github.com/sqlmapproject/sqlmap.git"]

# Installl dependencies
print("Installing deb packages")
res = subprocess.getoutput('sudo apt install vim curl unzip git make gcc -y')
print(res)

# vimrc updates
vimrc_text="set number\nset hlsearch\nsyntax on\nfiletype indent on"
vimrc_file=f"{os.environ['HOME']}/.vimrc"

if not os.path.exists(vimrc_file):
    with open(vimrc_file,'w') as f:
        print(f"Writing {vimrc_file}")
        f.write(vimrc_text)

# Define the tools directory
tools_dir = f"{os.environ['HOME']}/tools"

# Create the tools dir
if not os.path.exists(tools_dir):
    print(f"Creating tools dir: {tools_dir}")
    os.mkdir(tools_dir)

os.chdir(tools_dir)

# Clone the repos
for repo in REPOS:
    tool = repo.split('/')[4].replace('.git','')

    # If the tool exists, don't try to clone the repo
    if not os.path.exists(f"{tools_dir}/{tool}"):
        print(f"\nCloning {tool}\n")
        res = subprocess.getoutput(f"git clone {repo}")
        print(f"Result: {res}")

    # compile masscan
    if "masscan" in repo:
        if not os.path.exists(f"{tools_dir}/masscan/bin/masscan"):
            print("Compiling masscan...")
            os.chdir(f"{tools_dir}/{tool}")
            res = subprocess.getoutput("make -j")

            for ln in res.split("\n"):
                print(f"masscan_log: {ln}")

# Install httpx
if not os.path.exists(f"{tools_dir}/httpx"):
    print("Setting up httpx")
    os.chdir(tools_dir)
    #arch = f"{os.uname()[-1]}"
    arch = os.uname().machine

    if "aarch" in arch.lower():
        print(f"ARM detected")
        arch = "arm64"
    if "amd64" or "x86_64" in arch.lower():
        arch = "amd64"
        print(f"x64 detected")

    httpx_url = f"https://github.com/projectdiscovery/httpx/releases/download/v1.6.6/httpx_1.6.6_linux_{arch}.zip"
    subprocess.getoutput(f"curl -LO {httpx_url}")
    httpx_zip = httpx_url.split("/")[-1]
    subprocess.getoutput(f"unzip {httpx_zip} -d httpx")
    os.chdir('httpx')
    res = subprocess.getoutput(f"./httpx -up")
    for ln in res.split("\n"):
        print(f"httpx_log: {ln}")
    os.unlink(f"{tools_dir}/{httpx_zip}")

