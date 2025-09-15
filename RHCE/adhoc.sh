#!/bin/bash

ansible all -m ansible.builtin.yum_repository -a \
'name=MyBase description="base software" baseurl="http://192.168.10.10/pkg/BaseOS/" gpgcheck=false enabled=true'

ansible all -m ansible.builtin.yum_repository -a \
'name=MyAppStream description="AppStream software" baseurl="http://192.168.10.10/pkg/AppStream/" gpgcheck=false enabled=true'