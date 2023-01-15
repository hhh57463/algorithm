# 처음에 그냥 큐 형식으로 했더니 시간초과 발생
# 검색해보니 deque 방식을 사용하면 pop(0) 대신 popleft를 사용하면 된다함
# rotate(1) : 오른쪽으로 한칸 이동
# rotate(-1) : 왼쪽으로 한칸 이동
import sys
from collections import deque

N=int(sys.stdin.readline())
L=[i+1 for i in range(N)]
Q=deque(L)


while len(Q) > 1:
    Q.popleft()
    Q.rotate(-1)
print(Q[0])