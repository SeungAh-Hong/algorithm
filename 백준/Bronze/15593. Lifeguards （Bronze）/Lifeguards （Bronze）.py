# [15593] Lifeguards (브론즈 2)
N = int(input())
lifeguards = [list(map(int, input().split())) for _ in range(N)]
lifeguards.sort(key=lambda x:(x[0],x[1]))

ans = 0
for n in range(N):
    check = [0]*1001
    tmp = 0
    for i in range(len(lifeguards)):
        if i==n:
            continue
        s, e = lifeguards[i]
        for j in range(s, e):
            if check[j] == 0:
                check[j] += 1
                tmp += 1
    ans = max(ans, tmp)

print(ans)