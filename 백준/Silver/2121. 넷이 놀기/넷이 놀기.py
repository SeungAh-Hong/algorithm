# [2121] 넷이 놀기 (실버 2)
import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
## x, y
# x+a, y
# x+a, y+b
# x, y+b
nums = []
for _ in range(N):
    x, y = map(int, input().split())
    nums.append([x, y])

nums.sort(key=lambda x:(x[0], x[1]))

def find(x, y): # 이분탐색으로 고치기
    xy = [x, y]
    s = 0
    e = len(nums)-1

    while s <= e:
        m = (s+e)//2
        if nums[m] == xy:
            return True
        elif nums[m] < xy:
            s = m+1
        elif nums[m] > xy:
            e = m-1
    return False

ans = 0

for num in nums:
    x, y = num
    if find(x+a, y) and find(x+a, y+b) and find(x, y+b):
        ans+=1

print(ans)