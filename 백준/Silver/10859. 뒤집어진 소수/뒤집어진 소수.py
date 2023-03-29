# [10859] 뒤집어진 소수 (실버2)
import math
N = str(input())

num = int(N)
flag = True
if num < 2:
    flag=False
if flag:
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
            break

n_list = []
if flag:
    for i in range(len(N)-1, -1, -1):
        n = N[i]
        if n == '6':
            n_list.append('9')
        elif n == '9':
            n_list.append('6')
        elif n == '3' or n=='4' or n=='7':
            flag = False
            break
        else:
            n_list.append(n)

if flag:
    new_n = ''.join(str(n) for n in n_list)
    new_n = int(new_n)
    if new_n < 2:
        flag=False
    else:
        for i in range(2, int(math.sqrt(new_n))+1):
            if new_n % i == 0:
                flag = False
                break

if flag:
    print("yes")
else:
    print("no")