# 백준 10816 숫자 카드 2 (Counter)
import sys
input = sys.stdin.readline
from collections import Counter
N = int(input()) ## 상근이가 갖고 있는 카드 전체 개수
nList = Counter(map(int, input().split())) ## 숫자 카드


M = int(input()) ## 몇 개 갖고 있는지 구하려는 숫자 카드의 개수
mList = list(map(int, input().split())) ## 구하려는 숫자 카드의 값 리스트

for m in mList:
    if m in nList:
        print(nList[m])
    else:
        print(0)