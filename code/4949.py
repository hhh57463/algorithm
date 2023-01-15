# sys.stdin.readline()은 한문장 입력 후 개행문자(\n)까지 입력을 받는다
# 다 풀어놓고 계속 틀렸다고 나오길레 다시 확인해보니 스택이 비어있지도 않은데 맞았다고 함
import sys

while True:
    L=sys.stdin.readline()
    S=[]
    result=True
    if L=='.\n':
        break
    for i in L:
        if i == '(' or i == '[':
            S.append(i)
        if i == ')':
            if len(S) > 0:
                if S.pop(len(S)-1) != '(':
                    result=False
                    break
            else:
                result=False
                break
        elif i == ']':
            if len(S) > 0:
                if S.pop(len(S)-1) != '[':
                    result=False
                    break
            else:
                result=False
                break
    if len(S) != 0:
        result=False
    if result:
        print('yes')
    else:
        print('no')