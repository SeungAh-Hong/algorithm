#[1254] 팰린드롬 만들기

s = list(map(str, input()))

for i in range(len(s)):
    if s[i:] == s[i:][::-1]: # 팰린드롬 찾은 경우
        print(len(s)+i) # i부터 끝까지는 팰린드롬 + i까지를 뒤에 붙여주면 팰린드롬 완성
        break