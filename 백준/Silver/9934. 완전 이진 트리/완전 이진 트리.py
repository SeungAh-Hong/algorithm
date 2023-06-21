# [9934] 완전 이진 트리
import sys
input = sys.stdin.readline

k = int(input())
numbers = list(map(int, input().split()))

tree = [[] for _ in range(k)]

def makeTree(arr, x):
    mid = len(arr)//2
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

makeTree(numbers, 0)

for i in range(k):
    print(*tree[i])