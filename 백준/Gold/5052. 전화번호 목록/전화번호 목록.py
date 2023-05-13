# [5052] 전화번호 목록

import sys
input = sys.stdin.readline

# 전화번호 목록이 주어질 때, 이 목록이 일관성이 있는지 없는지를 구하기
## 일관성 유지하려면 한 번호 전체가 다른 번호의 접두어인 경우가 없어야 함

# 풀이
### 번호마다 다른 번호에 포함되는지 확인?

tc = int(input())

while tc > 0:
    N = int(input()) # 번호 수
    calls = []

    for _ in range(N):
        calls.append(input().strip())

    calls.sort()

    flag = True
    for i in range(N-1):
        long = len(calls[i])
        
        if calls[i] == calls[i+1][:long]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
    
    tc -= 1
