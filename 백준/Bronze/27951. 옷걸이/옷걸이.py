# [27951] 옷걸이
import sys
input = sys.stdin.readline

n = int(input())
hangers = list(map(int,input().split()))
u, d = map(int, input().split())

u_hanger = hangers.count(1)
d_hanger = hangers.count(2)

u_all = u-u_hanger
d_all = d-d_hanger

for i in range(len(hangers)):
    if hangers[i] == 1:
        hangers[i] = 'U'
        u -= 1
    elif hangers[i] == 2:
        hangers[i] = 'D'
        d -= 1
    else:
        if u_all > 0:
            hangers[i] = 'U'
            u -= 1
            u_all -= 1
        elif d_all > 0:
            hangers[i] = 'D'
            d -= 1
            d_all -= 1
        

if u == 0 and d == 0:
    print("YES")
    print(''.join(hangers))
else:
    print("NO")