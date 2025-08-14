#!/bin/ksh

if [ $# -ne 2 ]; then   
    echo "Usage : $0 <pattern> <filename>"
    exit 1 
fi
PATTERN=$1
FILENAME=$2
#echo "$PATTERN - $FILENAME"

grep "$PATTERN" "$FILENAME" > /dev/null 2>&1 
if [ $? -eq 0 ]; then 
    echo "[  OK  ] $FILENAME 파일에서 $PATTERN을 찾았습니다"
else    
    echo "[  OK  ] $FILENAME 파일에서 $PATTERN을 찾지 못했습니다"
fi