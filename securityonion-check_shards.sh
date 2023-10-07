#!/bin/bash

curl -sk https://localhost:9200/_cat/shards -u "username:password"

# Expected output:
#
# so-zeek-2023.05.12                  1 p STARTED  202779    231mb 10.1.1.10 securityonion
# so-ids-2023.06.29                   0 p STARTED    8310   12.8mb 10.1.1.10 securityonion
#
# ... etc
