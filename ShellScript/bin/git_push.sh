#!/bin/bash
#Usage : git_push.sh

if [ $# -ne 0 ]; then  
    echo "Usage $0 "
    exit
fi

BASEDIR=/project/Linux
cd "$BASEDIR"

# 환경변수 로드
source /root/bin/.env

# 프로젝트 디렉터리 구성
cat << EOF
#######################################################
* 프로젝트 디렉터리에 올리고 싶은 파일을 복사해주세요.
* 제외할 파일이 있다면 .gitignore 파일에 추가하세요.
#######################################################
EOF

echo "아무키나 누르면 다음으로 진행합니다."
read 

echo -n "[  INFO  ] 완료가 되었나요?  (y / n) "
read ANSWER

case $ANSWER in
    y) echo "[  OK  ] 다음을 진행합니다. " ;;
    *) echo "[  INFO  ] 프로그램을 종료합니다."
       exit 1 ;; 
esac

# 1. 모든 변경 사항 추가 (git add)
echo "모든 변경 사항을 추가합니다 ..."
if ! git add . ; then   
    echo "[  FAIL  ] 변경 사항 추가 실패"
    exit 1
fi

git status
echo "스테이징 된 파일을 확인하세요."
echo -n "[  INFO  ] 이대로 커밋을 진행할까요?  (y / n) "
read ANSWER

case $ANSWER in
    y) echo "[  OK  ] 다음을 진행합니다. " ;;
    *) echo "[  INFO  ] 스테이징을 취소하고 프로그램을 종료합니다."
       git reset .
       exit 1 ;;
esac

# 2. 커밋 작업
echo -n "[  INFO  ] 커밋 메세지를 작성해주세요 :  "
read COMMIT

if ! git commit -m "$COMMIT"; then
    echo "[ FAIL ] 커밋 실패"
    exit 1
fi

echo "원격 저장소의 최신 변경 사항을 가져옵니다..."
if ! git fetch; then
    echo "[ FAIL ] fetch 실패. 네트워크 연결 또는 저장소를 확인하세요."
    exit 1
fi

# 3. 푸시 전 로컬과 원격 브랜치 동기화 상태 확인
UPSTREAM=$(git rev-parse --abbrev-ref --symbolic-full-name @{u})
LOCAL=$(git rev-parse @{0})
REMOTE=$(git rev-parse @{u})

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "[ FAIL ] 로컬 브랜치가 최신 상태가 아닙니다. pull 후 충돌을 해결하세요."
    exit 1
fi

# 4. git push 인증 자동화
echo "원격 저장소에 푸시합니다..."
git remote set-url origin https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/username/repo.git
git push

echo "[ OK ] 푸시 완료."
