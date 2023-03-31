# [23888] 등차수열과 쿼리 (실버 1)
import sys
input = sys.stdin.readline
a, d = map(int, input().split())
q = int(input())

def CMD1(s, e):
    val = 0
    for i in range(s, e+1):
        val += A[i]
    return val

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def CMD2(s, e):
    gcd_val = A[s]
    for i in range(s+1, e+1):
        gcd_val = GCD(gcd_val, A[i])
    return gcd_val

cmd_list = []
a_list = []
max_idx = 0
for _ in range(q):
    cmd, s, e = map(int, input().split())
    if max_idx < e:
        max_idx = e
    cmd_list.append([cmd, s, e])

A = [0, a]
val = a
for i in range(1, max_idx):
    val += d
    A.append(val)

for cmd, s, e in cmd_list:
    if cmd == 1:
        print(CMD1(s, e))
    elif cmd == 2:
        print(CMD2(s, e))