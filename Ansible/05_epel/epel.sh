#!/bin/bash

BASEDIR=/home/ansible/ansible/05_epel
cd $BASEDIR

# 1) ansible.cfg 파일이 없으면 생성
[ ! -f ansible.cfg ] && cat << EOF > ansible.cfg
[defaults]
inventory = ./inventory

[privilege_escalation]
become = true
EOF

# 2) inventory 파일 생성
[ ! -f inventory ] && cat << EOF > inventory
ansible1
ansible2
ansible3
ansible4
EOF

# 3) 플레이북 실행
ansible-playbook epel.yml

