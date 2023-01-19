import sys

N,M=map(int, sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))

start=1
end=max(L)

while start<=end:
    mid = (start+end)//2
    tree=0
    for i in L:
        if i >= mid:
            tree+=i-mid
    if tree >= M:
        start=mid+1
    else:
        end=mid-1
print(end)