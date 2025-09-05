#!/bin/bash

WORKDIR=/home/ansible/ansible/00_poweroff
cd "$WORKDIR"

# 1) ansible.cfg 파일 생성
cat << EOF > ansible.cfg
[defaults]
inventory =  ./inventory

[privilege_escalation]
become = true
EOF

# 2) inventory 파일 생성
> inventory
NET=192.168.10
for i in 11 12 13 14
do 
    ping -c 1 -W 1 "$NET.$i" > /dev/null 2>&1
    [ $? -eq 0 ] && echo "$NET.$i" >> inventory
done

# 3) 플레이북 실행
ansible-playbook targethost.yml
sleep 5
ansible-playbook controlnode.yml