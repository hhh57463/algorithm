# 오랜만에 풀어봤는데 도저히 모르겠어서 검색했음
# 수학을 좀 알아야 할 듯함
import math

t = int(input())
s = []
a = []
gcd = 0
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)
a.append(gcd)
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')