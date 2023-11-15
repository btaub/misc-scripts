#!/bin/bash

if [[ -z $1 ]];then echo
    echo "Need domain name"
    exit
else
    DOMAIN=$1
fi

for NS in $(dig -tns $DOMAIN +short); do
	echo -e "$NS: $(dig +short @$NS version.bind txt ch)"
done
