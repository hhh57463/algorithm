# 시간초과 뜸 대전 가면 이거먼저 풀어보기로 하자
import sys

N=int(sys.stdin.readline().rstrip())
M=[int(sys.stdin.readline()) for _ in range(N)]

cnt=2
end=max(M)
result=[]

while cnt <= end:
    l=[]
    flag=True
    for i in range(N):
        if i == 0:
            l.append(M[i]%cnt)
        else:
            if M[i] % cnt not in l:
                flag=False
                break

    if flag:
        result.append(cnt)
    cnt+=1

for i in result:
    print(i, end=' ')