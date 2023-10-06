# [10773] 제로 (실버 4)
# 구현, 자료구조, 스택
import sys
input = sys.stdin.readline

k = int(input())
queue = []
for _ in range(k):
    num = int(input())
    if num == 0 and queue:
        queue.pop()
    else:
        queue.append(num)

print(sum(queue))