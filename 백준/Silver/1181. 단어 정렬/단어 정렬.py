import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr = set(arr)
arr = sorted(arr, key=lambda x:(len(x), x))

for a in arr:
    print(a)