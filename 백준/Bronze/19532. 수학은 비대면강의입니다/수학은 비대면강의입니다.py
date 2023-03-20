# [19532] 수학은 비대면강의입니다 (브론즈 2)
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            ans_x = x
            ans_y = y
            break

print(ans_x, ans_y)