## 10815 숫자 카드 (이분 탐색)

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

c_dict = {}
for num in cards:
    c_dict[num] = 1

m = int(input())
m_cards = list(map(int, input().split()))

for i in m_cards:
    if i in c_dict:
        print("1", end=' ')
    else:
        print("0", end=' ')
