import socket

ip = '192.168.10.60'
port = 21

s = socket.socket()  # 소켓 생성
s.connect((ip, port))  # 소켓 커넥션 설정
ans = s.recv(1024) # 버퍼 크기 1024로 지정
# print(ans)

if 'vsFTPd 2.0.5' in str(ans):
    print("[+] 'CWD' (Authenticated) Remote Memory Consumption")
elif 'vsFTPd 2.3.2' in str(ans):
    print("[+] Denial of Service")
elif 'vsFTPd 2.3.4' in str(ans):
    print("[+] Backdoor Command Execution (Metasploit)")
else:
    print('[-] FTP Server is not vulnerable.')
