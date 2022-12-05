# 1439 뒤집기
## 0이랑 1 나눈 후 더 작은 수 return
S = input()
zero = S.split('1')
one = S.split('0')
zero = ' '.join(zero).split()
one = ' '.join(one).split()

if len(zero) <= len(one):
    print(len(zero))
else:
    print(len(one))
