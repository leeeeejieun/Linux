#!/bin/bash

PASSWD=/etc/passwd

_Menu() {
    cat << EOF

(관리 목록)
------------------------------------
1) 사용자 추가
2) 사용자 확인
3) 사용자 삭제
4) 종료
------------------------------------
EOF
}

_UserAdd() {

    echo "(사용자 추가)"
    echo -n "추가할 사용자 이름? : "
    read NAME
    useradd $NAME > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
    echo "------------------------------------"
    echo "[  OK  ] 정상적으로 추가 되었습니다."
    echo "------------------------------------"

    echo $NAME | passwd --stdin $NAME > /dev/null 2>&1
    else
        echo "---------------------------------------"
        echo "[  FAIL ] 정상적으로 추가 되지 않았습니다."
        echo "---------------------------------------"
    fi
}

_USERVerify() {
    echo
    echo "(사용자 확인)"
    echo "------------------------------------"
    awk -F: '$3 >= 1000 && $3 <= 60000 {print $1}' $PASSWD | nl | sed 's/^    //'
    echo "------------------------------------"
}

_UserDel() {
    echo
    echo "(사용자 삭제)"
    echo "------------------------------------"
    echo -n "삭제할 사용자 이름? : "
    read NAME
    userdel -r $NAME > /dev/null 2>&1

    if [ $? -eq 0 ]; then
    echo "------------------------------------"
    echo "[  OK  ] 정상적으로 삭제 되었습니다."
    echo "------------------------------------"

    echo $NAME | passwd --stdin $NAME > /dev/null 2>&1
    else
        echo "---------------------------------------"
        echo "[  FAIL ] 정상적으로 삭제 되지 않았습니다."
        echo "---------------------------------------"
    fi
}

_ERROR() {
    echo "[ FAIL ]  "
} 

while true 
do
    _Menu
    echo -n "선택 번호?(1|2|3|4) : "
    read NUM

    case $NUM in
    1) _UserAdd ;;
    2) _USERVerify ;;
    3) _UserDel ;;
    4) exit ;;
    *) _ERROR ;;
    esac
done