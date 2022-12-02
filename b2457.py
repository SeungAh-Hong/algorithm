## 공주님의 정원 (그리디)

import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for i in range(n):
    s_mon, s_day, e_mon, e_day = map(int, input().split())
    start = s_mon*100 + s_day
    end = e_mon*100 + e_day
    flowers.append(list([start, end]))

flowers = sorted(flowers, key=lambda x:(x[0], x[1]))
# for i in range(n):
#     print(flowers[i])

end = 301 ## 시작지점이자 update될 end 지점
ans = 0
while(flowers): ## 모든 꽃에 대해 확인 (배열 삭제해가면서 while문 돎)
    if flowers[0][0] > end or end >= 1201: ## end 지점보다 시작지점이 크거나 1130 넘으면 종료
        break

    # 가장 느리게 지는 꽃 날짜 (update 시킬 변수)
    tmp_end = -1
    for _ in range(len(flowers)): ## 존재하는 flowers에 대해 전부 비교
        if flowers[0][0] <= end:
            if tmp_end <= flowers[0][1]:
                tmp_end = flowers[0][1]
            ## 선택 꽃부터 비교할꺼니까 해당 꽃까지 다 지움
            flowers.remove(flowers[0])
        else: ## 그 이후 꽃들
            break
    
    end = tmp_end
    ans += 1

if end < 1201:
    print(0)
else:
    print(ans)

