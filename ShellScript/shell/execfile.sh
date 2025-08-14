#!/bin/ksh

echo -e "파일 이름 입력 ? : \c"
read FILENAME

echo
if [ -x $FILENAME ]; then
    . $FILENAME
fi