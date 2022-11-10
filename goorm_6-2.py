## 구름 챌린지 6주차 2. 제곱암호
# from string import ascii_lowercase
# al_dict = {}
# a = 0
# for i in ascii_lowercase:
#     al_dict[i] = a
#     a += 1

n = int(input())
encr = input()
## 두 글자씩 떼오기
encr_list = [encr[i:i+2] for i in range(0, len(encr), 2)]
# print(encr_list)
decr_list = []

for en in encr_list:
    al = en[0]
    num = int(en[1])
    num = num ** 2
    ascii = ord(al) - 97
    ascii += num
    ascii %= 26
    ascii += 97
    al = chr(ascii)
    decr_list.append(al)

for i in decr_list:
    print(i, end='')