## 1541 잃어버린 괄호

## 최소값 만들기
# - 나오면 그 이후의 연산을 전부 해준 다음 그 앞까지의 연산값에서 빼줌

import sys
input = sys.stdin.readline

formula = list(input().rstrip().split('-'))
ans = 0
for i in formula[0].split('+'):
    ans += int(i)

for i in formula[1:]: ## - 가 나온 부분들마다 자름
    for j in i.split('+'):
        ans -= int(j)

print(ans)
