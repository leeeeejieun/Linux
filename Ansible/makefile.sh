#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <yumlfile>"
fi

mkdir -p ~/ansible/$1 && cd ~/ansible/$1

touch ansible.cfg
cat << EOF > ansible.cfg
[defaults]
inventory = ./inventory
remote_user = ansible
ask_pass = false

[privilege_escalation]
become = true
become_method = sudo
become_user = root
become_ask_pass = false
EOF

touch inventory
touch $2