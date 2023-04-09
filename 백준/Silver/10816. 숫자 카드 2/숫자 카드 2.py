# 백준 10816 숫자 카드 2 (이분 탐색)
import sys
input = sys.stdin.readline

N = int(input()) ## 상근이가 갖고 있는 카드 전체 개수
nList = list(map(int, input().split())) ## 숫자 카드 (정렬해서 넣어줌)

nDict = {}
for num in nList:
    if num not in nDict:
        nDict[num] = 1
    else:
        nDict[num] += 1

# print(nDict)

M = int(input()) ## 몇 개 갖고 있는지 구하려는 숫자 카드의 개수
mList = list(map(int, input().split())) ## 구하려는 숫자 카드의 값 리스트

for m in mList:
    if m in nDict:
        print(nDict[m])
    else:
        print(0)