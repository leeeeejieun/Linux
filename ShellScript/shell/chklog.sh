#!/bin/bash

#변수 설정
LOGFILE=/var/log/messages
TMP1=/tmp/tmp1
TMP2=/tmp/tmp2
TMP3=/tmp/tmp3
EMAIL=root

# 선수 패키지 설치
yum -y install postfix s-nail
/root/shell/svc.sh start postfix
#systemctl enable --now postfix

# 초기 로그 파일 생성
egrep -i '(warn|fail|error|crit|alert|emerg)' --color=auto "$LOGFILE" > "$TMP1"

# 30초에 한 번씩 로그 파일 점검
while true
do  
    sleep 10
    egrep -i '(warn|fail|error|crit|alert|emerg)' --color=auto "$LOGFILE" > "$TMP2"
    diff $TMP1 $TMP2 > $TMP3 && continue

    #관리자에게 메일 전송
    mailx -s "[CHECK] $LOGFILE check" $EMAIL < "$TMP3"
    # 초기 로그 파일 생성
    egrep -i '(warn|fail|error|crit|alert|emerg)' --color=auto "$LOGFILE" > "$TMP1"
done