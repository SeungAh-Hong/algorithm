# [6131] 완전 제곱수

N = int(input())
# 1 <= B <= A <= 500
## A*A == B*B + N 인 경우를 만족하는 A, B 쌍의 개수

count = 0

for b in range(1, 501):
    for a in range(b, 501):
        if a*a == b*b + N:
            count+=1

print(count)