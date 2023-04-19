# 1564 N과 M(1) # 백트래킹
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
# 1~n까지 자연수 중에서 중복 없이 m개를 고른 수열
lists = [] # 


# 방법 1. itertools 이용
import itertools
N = [i for i in range(1, n+1)]
lists = itertools.permutations(N, m)
answer = []
for arr in lists:
    answer.append(' '.join(map(str, arr)))

answer.sort()
for ans in answer:
    print(ans)
