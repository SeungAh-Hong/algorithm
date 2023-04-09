# [1484] 다이어트
G = int(input())
def cal(a, b):
    return a**2 - b**2

new, old = 2, 1
ans = []
while new+old <= G:
    if cal(new, old) == G :
        ans.append(new)
        new+=1
    elif cal(new, old) > G:
        old+=1
    elif cal(new, old) < G:
        new+=1

if len(ans) > 0:
    for a in ans:
        print(a)
else:
    print(-1)