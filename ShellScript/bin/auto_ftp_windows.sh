#!/bin/bash

FTPSERVER=192.168.10.1
ftp -n $FTPSERVER 21 << EOF
user user01 user01
lcd  /test
cd test
bin
hash
prompt
mput linux206.txt
quit
EOF