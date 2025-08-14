#!/bin/ksh

cat << EOF 
====================================================
  (1). who      (2). date     (3). pwd              
====================================================
EOF

echo -n "번호를 입력하세요(1-3). >  "
read NUMBER

echo
case "$NUMBER" in
    1) who ;;
    2) date ;;
    3) pwd ;;
    *) echo "Error ... Try Agin"
        exit 1 ;;
esac
echo
