# [16472] 고냥이 (골드 4)
import sys
input = sys.stdin.readline
N = int(input())
arr = input().rstrip()
dic = {}

answer = 0
l, r = 0, 0

if len(arr) == 1:
    answer = 1
else:
    while True:
        if l >= len(arr) or r >= len(arr):
            break

        dic.setdefault(arr[r], 0)
        dic[arr[r]] += 1
        
        while len(dic) > N:
            dic[arr[l]] -= 1
            if dic[arr[l]] == 0:
                del dic[arr[l]]
            l+=1
        
        answer = max(answer, r-l+1)
        r+=1

print(answer)