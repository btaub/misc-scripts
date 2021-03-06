#!/bin/bash

# Notes:
  # Grab running-config from switch and save to an IP-timestamp file in /tmp. 
  # The user this runs as must have level 15 access to the switch.

SWITCHES="192.168.0.3 192.168.0.4 192.168.0.5"
UA="User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"

for SW in $SWITCHES;
 do
    echo "Connecting to $SW"
# Login via https and get session cookie
COOKIE=$(curl -i -s -k  -X $'POST' -H $"$UA" -H $'Referer: https://'$SW'/htdocs/login/login.lsp' -H $'Content-Type: application/x-www-form-urlencoded' -H $'X-Requested-With: XMLHttpRequest' --data-binary $'username=Level15user&password=Level15pass&accept_eula=0&require_eula=0' $'https://'$SW'/htdocs/login/login.lua' | grep Cook |awk -F= {'print $2'} )

# Generate file to download
curl -i -s -k  -X $'POST' -H $"$UA" \
     -H $'Referer: https://'$SW'/htdocs/pages/base/file_upload_modal.lsp?filetypes=6&protocol=6' \
     -H $'Content-Type: application/x-www-form-urlencoded' \
     -H $'X-Requested-With: XMLHttpRequest' \
     -b $'SIDSSL='$COOKIE --data-binary $'file_type_sel%5B%5D=config' \
        $'https://'$SW'/htdocs/lua/ajax/file_upload_ajax.lua?protocol=6'>/dev/null


# Download config
curl -s -k  -X $'GET' -H $"$UA" \
     -H $'Referer: https://'$SW'/htdocs/pages/base/file_upload_modal.lsp?filetypes=6&protocol=6' \
     -H $'Upgrade-Insecure-Requests: 1' \
     -b $'SIDSSL'=$COOKIE \
        $'https://'$SW'/htdocs/pages/base/http_download_file.lua?filepath=/mnt/download/TempConfigScript.scr' -o /tmp/$SW"_"$(date +%Y%m%d%H%M)

done
