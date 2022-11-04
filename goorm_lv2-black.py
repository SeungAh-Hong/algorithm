## 구름 난이도 2 - 근묵자흑
## 경희대학교대회기출문제
import sys

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
idx = n_list.index(1)

answer = sys.maxsize ## 최대값
for i in range(k): ## 인덱스를 포함한 배열의 경우의 수
    cnt = 1
    front, back = n_list[:idx-i], n_list[idx+k-i:]
    if len(front)%(k-1) == 0:
        front_cnt=len(front)//(k-1)
    else:
        front_cnt=(len(front)//(k-1))+1

    if len(back)%(k-1) == 0:
        back_cnt=len(back)//(k-1)
    else:
        back_cnt=(len(back)//(k-1))+1
    
    answer = min(answer, cnt+front_cnt+back_cnt)

print(answer)