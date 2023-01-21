# 겁나 쉬어보였는데 푸는데 한시간 걸렸음
# 처음에 시간초과가 뜨고 pop이 시간이 오래걸린다는걸 생각하고
# 무작정 deque로 풀어봄
# 생각해보니 reverse도 비용이 비싸다고 들었던것 같아서 R의 갯수를 생객했음
# 새벽이라 그런지 머리가 잘돌아갔던것 같음
# join()부분은 검색해서 했음

import sys
from collections import deque

T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    p=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())
    I=sys.stdin.readline().rstrip()[1:-1].split(',')
    flag=True
    cnt=0
    if n > 0:
        Q=deque(I)
    else:
        Q=[]
    for i in p:
        if i == 'R':
            cnt+=1
        elif i == 'D':
            if len(Q) > 0:
                if cnt % 2 == 0:
                    Q.popleft()
                else:
                    Q.pop()
            else:
                flag=False
                break
    if flag:
        if cnt % 2 == 0:
           print("[" + ",".join(Q) + "]")
        else:
           Q.reverse()
           print("[" + ",".join(Q) + "]")
    else:
        print('error')