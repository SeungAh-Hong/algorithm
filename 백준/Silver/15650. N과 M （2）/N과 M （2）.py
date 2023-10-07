# [15650] N과M(2) (실버3)
import itertools
n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
arr = map(str, arr)
nCr = list(map(' '.join, itertools.combinations(arr, m)))

nCr = list(nCr)

for num in nCr:
    print(num)