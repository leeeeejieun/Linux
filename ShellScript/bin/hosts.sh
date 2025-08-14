#!/bin/bash

START=200
END=230
NET=172.16.6

#HOSTS=/etc/hosts
HOSTS=hosts
/bin/cp  /etc/hosts /root/bin/$HOSTS

# 등록된 상태를 다시 등록하지 않음
if grep -w -q linux206 "$HOSTS" ; then
    echo "[ INFO ] 내용이 이미 존재합니다."
fi

# 
IP=$(ip addr show ens192 | grep -w 'inet' | awk '{print $2}' | awk -F/ '{print $1}')

for i in $(seq $START $END)
do
    [ "$IP" -eq "$NET.$i" ] && continue
    echo "$NET.$i linux$i.example.com linux$i" >> $HOSTS
done

