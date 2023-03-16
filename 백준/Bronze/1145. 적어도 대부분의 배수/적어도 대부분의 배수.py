# [1145] 적어도 대부분의 배수 (브론즈 1)
import sys
input = sys.stdin.readline

iList = list(map(int, input().split()))

cnt = 0
num = 1
while True:
    tmp = 0
    for i in iList:
        if num % i == 0:
            tmp += 1
    
    if tmp >= 3:
        print(num)
        break
    else:
        num += 1
