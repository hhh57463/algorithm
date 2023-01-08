# 코드를 완성 했지만 더 괜찮은 코드가 있을까 찾아봤더니 while ~ else 라는 문법을 찾았다
# while의 조건이 맞지 않을 시 else 안의 코드를 실행
import sys
N=int(sys.stdin.readline())
result = 0

while N >= 0:
    if N % 5 == 0:
        result += N // 5
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)