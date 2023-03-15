

A, B = map(int, input().split())
answer = []
for x in range(-1000, 1001, 1):
    if x*x + 2*A*x + B == 0:
        answer.append(x)

answer = list(set(answer))
answer.sort()

for a in answer:
    print(a, end=' ')