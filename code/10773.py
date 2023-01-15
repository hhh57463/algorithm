import sys

K=int(sys.stdin.readline())
S=[]
result=0

for _ in range(K):
    N=int(sys.stdin.readline())
    if N==0:
        S.pop(len(S)-1)
    else:
        S.append(N)

for i in S:
    result+=i

print(result)