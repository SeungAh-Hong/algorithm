## 구름 챌린지 3. 비밀 편지
from string import ascii_lowercase
from string import ascii_uppercase

n = int(input())

for i in range(n):
    str = input()
    k = list(input().split())
    key = ""
    while (len(key) < len(str)):
        key += k[1]
    
    key = key[:len(str)]
    #print(key)
    ans_str = ""
    if k[0] == "E": ## Encrypt
        for i in range(len(str)):
            ascii = 0
            if str[i].isalpha(): ## 알파벳인지 확인
                if str[i].islower():
                    ## 소문자 확인
                    ascii = ord(str[i])
                    ascii -= 97
                    ascii += ord(key[i]) % 26
                    ascii %= 26
                    ascii += 97
                    al = chr(ascii)
                    ans_str += al
                elif str[i].isupper():
                    ## 대문자 확인
                    ascii = ord(str[i])
                    ascii -= 65
                    ascii += ord(key[i]) % 26
                    ascii %= 26
                    ascii += 65
                    al = chr(ascii)
                    ans_str += al

            else:
                ans_str += str[i]
    elif k[0] == "D": ## Decrypt
        for i in range(len(str)):
            ascii = 0
            if str[i].isalpha(): ## 알파벳인지 확인
                if str[i].islower():
                    ## 소문자 확인
                    ascii = ord(str[i])
                    ascii -= 97
                    #ascii -= ord(key[i]) % 26
                    ascii -= ord(key[i])
                    while(ascii < 0):
                        ascii += 26
                    ascii %= 26
                    ascii += 97
                    al = chr(ascii)
                    ans_str += al
                elif str[i].isupper():
                    ## 대문자 확인
                    ascii = ord(str[i])
                    ascii -= 65
                    # ascii += ord(key[i]) % 26
                    ascii -= ord(key[i])
                    while(ascii < 0):
                        ascii += 26
                    ascii %= 26
                    ascii += 65
                    al = chr(ascii)
                    ans_str += al

            else:
                ans_str += str[i]
        
    print(ans_str)