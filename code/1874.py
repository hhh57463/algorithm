import sys

N=int(sys.stdin.readline())

S=[]
result=[]
cnt=0
flag=True

for _ in range(N):
    sequence=int(sys.stdin.readline())

    while cnt < sequence:
        cnt+=1
        S.append(cnt)
        result.append('+')

    if S[-1] == sequence:
        S.pop()
        result.append('-')
    else:
        flag=False
        break

if flag:
    for i in result:
        print(i)
else:
    print('NO')