# 또 공식이 있는줄알고 계속 헤맸음
import sys
N = int(sys.stdin.readline())
room = 1
cnt = 1
while N > room:
    room += cnt*6
    cnt+=1
print(cnt)