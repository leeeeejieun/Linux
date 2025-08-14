#!/bin/ksh

if [ $# -ne 1 ] ; then
    echo "Usage : $0 filename"
    exit 1
fi
FILE=$1

FILESIZE=$(wc -c < $FILE)

if [ -s $FILESIZE ]; then
    if [ $FILESIZE -gt 5120 ]; then
        echo "$FILE($FILESIZE) : 5120 byte 보다 큰 파일입니다."
    elif [ $FILESIZE -le 5120 ]; then
        echo "$FILE($FILESIZE) : 5120 byte 보다 작은 파일입니다."
    fi
else   
    echo "빈 파일입니다."

