#!/bin/bash

echo -n "Enter A : "
read A
echo -n "Enter Operator(+-*/) : "
read OPT
echo -n "Enter B : "
read B
RESULT=0

case $OPT in
    '+') RESULT=$(expr $A + $B)  ;;
    '-') RESULT=$(expr $A - $B)  ;;
    '*') RESULT=$(expr $A \* $B) ;;
    '/') RESULT=$(expr $A / $B)  ;;
    *) echo "잘못된 입력입니다." ;;
esac
echo "$A $OPT $B = $RESULT"