# [1759] 암호 만들기
import sys
input = sys.stdin.readline

def backtracking(cnt, idx):
    # 예비 암호
    if cnt==L:
        vow, con = 0, 0
        for i in range(cnt):
            if ans[i] in vowel:
                vow+=1
            else:
                con+=1
        # 찐 암호
        if vow >= 1 and con >= 2:
            answers.append("".join(ans))

    for i in range(idx, C):
        ans.append(alph[i])
        backtracking(cnt+1, i+1)
        ans.pop()

L, C = map(int, input().split())
alph = sorted(list(map(str, input().split())))
# 서로다른L개. 1개모음(a,e,i,o,u) + 2개자음 이상
vowel = ['a', 'i', 'o', 'u', 'e']
answers = []
ans = []
backtracking(0, 0) # cnt_vowel, cnt_consonant

answers.sort()
for a in answers:
    print(a)