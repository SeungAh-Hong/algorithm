# 구름 알고리즘 챌린지 7주차 1. UXUI 디자이너

n, m = map(int, input().split())
## n: 이벤트 개수, m: 사용자 수
event_cnt = [0]*(n+2)
for i in range(m): ## 사용자 수만큼
    u_list = list(map(int, input().split()))
    u_list = u_list[1:]
    for u in u_list:
        event_cnt[u] += 1

ans_value = max(event_cnt)
ans_list = []
for i in range(len(event_cnt)):
    if event_cnt[i] == ans_value:
        ans_list.append(i)

ans_list.sort(reverse=True)
for i in ans_list:
    print(i, end=' ')