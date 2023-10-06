import sys
input = sys.stdin.readline

n = int(input())
flowers = []

for i in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append(list((start, end)))

flowers = sorted(flowers, key=lambda x:(x[0], x[1]))
end = 301
ans = 0
while(flowers):
    if flowers[0][0] > end or end >= 1201:
        break
    
    tmp = 0
    for _ in range(len(flowers)):
        if flowers[0][0] <= end:
            if tmp <= flowers[0][1]:
                tmp = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    end = tmp
    ans += 1

if end < 1201:
    print(0)
else:
    print(ans)