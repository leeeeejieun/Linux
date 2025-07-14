# (server1)
# (ㄱ) 스크립트 만들기
mkdir -p /root/bin

cat << EOF > /root/bin/backup.sh
#!/bin/bash

cd /home
tar cvzf /backup/home_\$(date +%m%d_%H%M%S).tar.gz . > /backup/backup.log 2>&1

EOF

# (ㄴ) 백업 스크립트 실행 권한 주기
chmod 700 /root/bin/backup.sh

# (ㄷ) 백업 대상 디렉토리 생성
mkdir -p /backup
rm -rf /backup/*
