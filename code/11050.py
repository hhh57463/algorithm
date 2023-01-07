import sys
from math import factorial

N,K = map(int, sys.stdin.readline().split())
R = factorial(N) // (factorial(K) * factorial(N-K))

print(R)