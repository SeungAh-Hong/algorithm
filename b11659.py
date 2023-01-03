## 11659 구간 합 구하기 4 (DP, 누적 합)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

pre_sum = [0]

tmp = 0
for num in nums:
    tmp += num
    pre_sum.append(tmp)

    
for i in range(m):
    a, b = map(int, input().split())
    print(pre_sum[b]-pre_sum[a-1])