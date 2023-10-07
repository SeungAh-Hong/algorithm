# 10814

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append([int(age), int(i), name])

arr = sorted(arr, key=lambda x:(x[0], x[1]))

for age, i, name in arr:
    print(age, name)