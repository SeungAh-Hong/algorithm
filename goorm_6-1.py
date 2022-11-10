# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
## 구름 챌린지 6주차 1.7게임

k_list = []
for i in range(5):
    k = list(map(int, input()))
    k_list.append(k)

# for i in range(5):
#     print(k_list[i])

for i in range(5):
    a = 0
    for j in range(0, 7, 2): ## 1~7까지 홀수 더함
        a += k_list[i][j]
    for j in range(1, 7, 2): ## 짝수일 때
        if k_list[i][j] != 0:
            a *= k_list[i][j]
    a = a % 10
    print(a)
        