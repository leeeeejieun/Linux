#!/bin/bash

START=200
END=230
NET=172.16.6

for i in $(seq $START $END)
do
    ping -c 1 -W 0.5 $NET.$i > /dev/null 2>&1 
    if [ $? -eq 0 ] ; then
        $(sed -i s/$i/OOO/ /root/bin/position.txt)
    else
        $(sed -i s/$i/XXX/ /root/bin/position.txt)
    fi
done
echo "파일 변경이 끝났습니다"
echo
cat /root/bin/position.txt
echo
