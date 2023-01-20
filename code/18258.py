# 쉬운줄 알고 꿀이네 하고 있었다가 시간초과 떠서 뇌정지
# list.pop()은 시간이 오래걸린다는것 같다
# 그래서 pop을 대신할 수 있는게 있을까 생각하다
# 인덱스 접근으로 짜보면 될 것같았는데 맞았음

import sys

N=int(sys.stdin.readline())
Q=[]
idx=0
for _ in range(N):
    C=list(map(str, sys.stdin.readline().split()))
    if C[0] == 'push':
        Q.append(int(C[1]))
    elif C[0] == 'pop':
        if len(Q)-idx == 0:
            print(-1)
        else:
            print(Q[idx])
            idx+=1
    elif C[0] == 'size':
        print(len(Q)-idx)
    elif C[0] == 'empty':
        if len(Q)-idx == 0:
            print(1)
        else:
            print(0)
    elif C[0] == 'front':
        if len(Q)-idx == 0:
            print(-1)
        else:
            print(Q[idx])
    elif C[0] == 'back':
        if len(Q)-idx == 0:
            print(-1)
        else:
            print(Q[-1])