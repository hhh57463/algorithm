# 백트래킹 (퇴각 검색)
# 길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행
# 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다.
# DFS(깊이 우선 탐색) 기반
import sys

N,M=list(map(int, sys.stdin.readline().split()))
L=[]

def DFS():
    if len(L) == M:
        print(' '.join(map(str,L)))
        return
    
    for i in range(1,N+1):
        if i not in L:
            L.append(i)
            DFS()
            L.pop()
DFS()