# 165 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())

lines = []
for i in range(k):
    lines.append(int(input()))

max_line = max(lines)

start = 1
end = max_line

while(start <= end):
    mid = (start+end)//2
    lan = 0 # 랜선 수
    for line in lines:
        lan += (line//mid) ## 랜선 분할
    
    if lan >= n: ## 랜선 개수가 원래 목표 n개보다 크면
        start = mid+1 # 키워서 다시 탐색

    else:
        end = mid-1 # 끝 좁혀서 다시 탐색

print(end)