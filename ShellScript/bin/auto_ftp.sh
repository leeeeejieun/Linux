#!/bin/bash

ftp -n 172.16.6.30 << EOF
user root soldesk1.
cd /tmp
lcd /test
bin
hash
prompt
mput linux230.txt
quit
EOF