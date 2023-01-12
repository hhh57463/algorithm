import sys

T=int(sys.stdin.readline())

for _ in range(T):
    H,W,N=map(int, sys.stdin.readline().split())
    A=N%H
    if A == 0:
        A = H
        B=N//H
    else:
        B=N//H + 1
    if int(B) < 10:
        print(str(A)+'0'+str(B))
    else:
        print(str(A)+str(B))