#!/bin/bash

TARGET=$1

echo -e "\n#####################"
echo    "#"
echo    "# Checking Shodan:"
echo    "#"
echo    "########################"
curl -s "https://internetdb.shodan.io/$TARGET" | jq

echo -e "\n----------------\n"

echo    "########################"
echo    "#"
echo    "# Checking IpInfo.io:"
echo    "#"
echo    "#######################"
curl -s "https://ipinfo.io/$TARGET" | jq

echo -e "\n----------------\n"

echo    "#######################"
echo    "#"
echo    "# Checking AlientVaultOTX:"
echo    "#"
echo    "#######################"
curl -s "https://otx.alienvault.com/otxapi/indicators/ip/general/$TARGET" | jq

echo -e "\n----------------\n"
