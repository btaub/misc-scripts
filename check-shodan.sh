#!/bin/bash

curl -s "https://internetdb.shodan.io/$1" | jq
