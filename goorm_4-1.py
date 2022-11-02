# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
## 구름 알고리즘 챌린지 4주차 - 1. 체크카드
from collections import deque


n, m = map(int, input().split())
account = n
queue = deque()

for i in range(m):
	func, money = input().split()
	money = int(money)
	
	if func == "deposit":
		account+=money
		while(queue and queue[0] <= account):
			account -= queue[0]
			queue.popleft()
	elif func == "pay":
		if (money <= account):
			account -= money
	elif func == "reservation":
		if (queue or money > account):
			queue.append(money)
		else:
			account-=money
			
print(account)
	