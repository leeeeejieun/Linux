#!/bin/ksh

echo -e "파일명을 입력하세요 >  \c"
read FILENAME

if [ -d $FILENAME ] ; then
    echo "[OK] 디렉터리 파일입니다."
elif [ -f $FILENAME ] ; then  
    echo "[OK] 일반 파일입니다."
else
    echo "[FAIL] 잘못된 파일입니다."
fi