#!/bin/ksh

echo -n "yes/no를 입력하세요 > " 
read ANSWER

case "$ANSWER" in   
    y | yes | Yes | YES | Y) echo "Yes를 입력하셨습니다." ;;
    n | no  | No  | NO  | N) echo "No를 입력하셨습니다." ;;
    *)  echo "잘못된 입력입니다."
        exit 1 ;;
esac
