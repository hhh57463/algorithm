import sys

N=int(sys.stdin.readline())
L=[]
for _ in range(N):
    X,Y = map(int, sys.stdin.readline().split())
    L.append((X, Y))

for i in L:
    score = 1
    for j in L:
        if i[0] < j[0] and i[1] < j[1]:
                score += 1
    print(score, end = " ")