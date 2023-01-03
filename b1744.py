## 1744 수 묶기

import sys
input = sys.stdin.readline
n = int(input())
plus = []
minus = []
for i in range(n):
    num = int(input())
    if num >= 1:
        plus.append(num)
    else:
        minus.append(num)

plus = sorted(plus, reverse=True)
minus = sorted(minus)
hap = []


## plus
while(plus):
    if len(plus) >= 2:
        if plus[0]==1: ## 1은 그냥 바로 더함
            hap.append(plus[0])
            plus.remove(plus[0])
        elif plus[1]==1:
            hap.append(plus[0])
            hap.append(plus[1])
            plus.remove(plus[0])
            plus.remove(plus[0])
        else:
            hap.append(plus[0]*plus[1])
            plus.remove(plus[0])
            plus.remove(plus[0])
    else:
        hap.append(plus[0])
        break

while(minus):
    if len(minus) >= 2:
        if minus[0]==0:
            minus.remove(minus[0])
            minus.remove(minus[-1])
        else:
            hap.append(minus[0]*minus[1])
            minus.remove(minus[0])
            minus.remove(minus[0])
    else:
        hap.append(minus[0])
        break


#print(hap)
print(sum(hap))