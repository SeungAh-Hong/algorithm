## 2847. 게임을 만든 동준이 (Greedy)
import sys
input = sys.stdin.readline

n = int(input())
score = [0]*n
for i in range(n):
    score[i] = int(input())

cnt = 0
for i in range(n-1, 0, -1):
    while score[i] <= score[i-1]:
        score[i-1] -= 1
        cnt += 1
print(cnt)
