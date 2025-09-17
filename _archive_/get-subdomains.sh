#!/bin/bash

if [[ -z "$1" ]]; then
    echo -e "\nGet list of subdomains from subdomain.center"
    echo -e "\nUsage: $0 example.com"
    echo -e "\n       Pass -o to write the output to example.com_subdomains.txt\n"
    exit
fi

if [[ $2 == "-o" ]]; then
  curl -s https://api.subdomain.center/?domain="$1" | jq -r '.[]' |sort > "$1_subdomains.txt"

else
  curl -s https://api.subdomain.center/?domain="$1" | jq -r '.[]' | sort
fi
