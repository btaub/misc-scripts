#!/bin/bash

TARGET=$1

echo "##################"
echo "#"
echo "# Checking Shodan:"
echo "#"
echo "##################"
curl -s "https://internetdb.shodan.io/$TARGET" | jq

echo "\n----------------\n"

echo "#####################"
echo "#"
echo "# Checking IpInfo.io:"
echo "#"
echo "#####################"
curl -s "https://ipinfo.io/$TARGET" | jq
