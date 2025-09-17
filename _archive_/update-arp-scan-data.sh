#!/bin/bash

updatepath="/usr/share/arp-scan"

# Have to be root to write the files
if [[ $(whoami) != "root" ]]; then
    echo -e "\nYou need root for this to work \n"
    exit
fi

# To be used if non-standard path
function find_it()
{
if [[ $(which locate) ]]; then
    loc=$(locate ieee-oui.txt)
    updatepath=$(dirname $loc)
fi
}

# Non-zero file in the dir? We should be good to proceed
if [[ -s $updatepath/ieee-oui.txt ]] ; then
    echo "Update path is $updatepath"
else
    find_it
fi

# Change dir and run the update 
if [[ $updatepath ]]; then
   # cd to the dir where the file is stored 
   cd $updatepath
   echo "Running update now...please wait"

# Update the files using the arp-scan-provided utils
    get-oui -u http://standards-oui.ieee.org/oui/oui.txt
    get-iab -u http://standards-oui.ieee.org/iab/iab.txt
fi
