import sys
from collections import Counter

N,M,B = map(int, sys.stdin.readline().split())

ground = []
for _ in range(N): ground += map(int, sys.stdin.readline().split())
height, time = 0, 1000000000000000

min_h = min(ground)
max_h = max(ground)
S = sum(ground)
ground = dict(Counter(ground))

for i in range(min_h, max_h + 1):
    if S + B >= i * N * M:
        cur_time = 0
        for key in ground:
            if key > i:
                cur_time += (key - i) * ground[key] * 2
            elif key < i:
                cur_time += (i - key) * ground[key]
        if cur_time <= time:
            time = cur_time
            height = i

print(time, height)