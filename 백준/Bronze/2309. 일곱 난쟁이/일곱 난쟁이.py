# [2309] 일곱 난쟁이 (브론즈 1)
import sys
input = sys.stdin.readline

nine = [int(input()) for _ in range(9)]
nine = sorted(nine)

height = sum(nine)

a, b = 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if height-nine[i]-nine[j] == 100:
            a = i
            b = j
            break

## nine 에서 a, b만 제외하고 출력
nine[a] = nine[b] = 0
answer = []
for h in nine:
    if h == 0:
        continue
    answer.append(h)

answer = sorted(answer)
for a in answer:
    print(a)