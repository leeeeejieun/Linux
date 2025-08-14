#!/bin/bash

cd /root/bin
cat << EOF > $1.sh
#!/bin/bash


EOF
chmod 755 /root/bin/*.sh