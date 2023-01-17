# 변수를 너무 최소화해서 구현하려 한다는 것을 느꼈음
# 어짜피 문제 풀때는 용량을 신경쓰지도 않는데 너무 변수를 최소화 하려 하지 않기

import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    N,M=map(int, sys.stdin.readline().split())
    Q=deque(list(map(int, sys.stdin.readline().split())))
    L=deque(list(range(N)))
    cnt=0
    while True:
        if Q[0] == max(Q):
            Q.popleft()
            idx=L.popleft()
            cnt+=1
            if idx == M:
                print(cnt)
                break
        else:
            Q.append(Q.popleft())
            L.append(L.popleft())