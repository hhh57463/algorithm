# 이분탐색이 뭔지는 알았지만 정확히 알지 못해서 검색해서 풀었음
# 이분탐색의 원리를 이해하는데 힘썼음
import sys

K,N=map(int, sys.stdin.readline().split())
L=[int(sys.stdin.readline()) for _ in range(K)]
start=1
end=max(L)

while start <= end:
    mid = (start+end)//2
    lan=0
    for i in L:
        lan+=i//mid
    if lan>=N:
        start=mid+1
    else:
        end=mid-1
print(end)