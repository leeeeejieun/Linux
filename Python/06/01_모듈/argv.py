import sys

print(sys.argv) 			# 인자 전체
print(sys.argv[0])		# 첫 번째 인자 : 명령어
print(sys.argv[1])		# 두 번째 인자 : 명령어의 첫 번째 인자
print(sys.argv[2])		# 세 번째 인자 : 명령어의 두 번째 인자.
print(sys.argv[3])		# 네 번째 인자 : 명령어의 세 번째 인자.
print(len(sys.argv))		# 전체 인자의 개수
print(len(sys.argv[1:]))	# 명령어의 총 인자 개수
