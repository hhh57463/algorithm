import sys
from collections import Counter

N=int(sys.stdin.readline())
L=[]
result=[0 for _ in range(4)]
for _ in range(N):
    L.append(int(sys.stdin.readline()))

L.sort()

for i in L:
    result[0]+=i
result[0]=round(result[0]/N)
result[1]=L[int(len(L)/2)]
result[2]=Counter(L).most_common(2)
if len(result[2]) > 1:
    if result[2][0][1] == result[2][1][1]:
        result[2]=result[2][1][0]
    else:
        result[2]=result[2][0][0]
else:
    result[2]=result[2][0][0]
result[3]=L[-1]-L[0]

print(result[0])
print(result[1])
print(result[2])
print(result[3])