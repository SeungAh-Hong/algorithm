# [15650] N과M(2) (실버3)
# import itertools
# n, m = map(int, input().split())
# arr = [i for i in range(1,n+1)]
# arr = map(str, arr)
# nCr = list(map(' '.join, itertools.combinations(arr, m)))

# nCr = list(nCr)

# for num in nCr:
#     print(num)

## 다른 풀이
from itertools import combinations
n, m = map(int, input().split())
for i in combinations([i for i in range(1, n+1)], m):
    print(*i)

# print(*): 리스트 원소나 문자열 각각의 문자를 한 칸 씩 띄운 후(공백) 출력