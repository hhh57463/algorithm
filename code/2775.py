# 풀긴 풀었는데 개오래걸렸음 (수학공식이 있는지 생각을 해서 그랬음)
# 아무리 봐도 수학 공식이 없어 보일 경우 그냥 짜보는 습관 들이기
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    L=[x+1 for x in range(N)]
    for i in range(K):
        for j in range(1, N):
            L[j]+=L[j-1]
    print(L[-1])