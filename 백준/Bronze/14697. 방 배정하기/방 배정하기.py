# [14697] 방 배정하기 (브론즈 2)


A, B, C, N = map(int, input().split())
answer = 0
for a in range(51):
    for b in range(51):
        for c in range(51):
            if A*a + B*b + C*c == N:
                answer = 1
                break

print(answer)