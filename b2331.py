# 2331 반복수열 (수학, 구현)

input = list(map(int, input().split()))
A = input[0]
P = input[1]

## 같은 수 나온 순간 해당 인덱스 앞까지 배열 자르기
dlist = []
dlist.append(A)
now_num = A

while 1:
    next_num = 0
    while (now_num != 0):
        next_num += int(pow(now_num%10, P))
        now_num = now_num//10 ## 몫 //
    if next_num in dlist:
        break
    else:
        dlist.append(next_num)
    now_num = next_num

idx = dlist.index(next_num)
print(idx)