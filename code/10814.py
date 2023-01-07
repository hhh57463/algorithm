import sys

L = []
N = int(sys.stdin.readline())
for i in range(N):
    L.append(list(sys.stdin.readline().split()))

L.sort(key=lambda a:int(a[0]))

for i in range(len(L)):
    print(L[i][0] + ' ' + L[i][1])