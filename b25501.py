## 25501 재귀의 귀재

def recursion(s, l, r): ## 재귀함수
    global cnt
    cnt+=1
    # s : 문자열, l : 0부터 시작하는 idx, r : -1부터 시작하는 idx
    if l >= r: return 1 # 앞-뒤 인덱스가 겹치면 종료
    elif s[l] != s[r]: return 0 # 재귀가 아닌 경우
        ## 앞 <-> 뒤 idx 해당하는 값 비교
    else: return recursion(s, l+1, r-1) ## 일치하면 다시 recursion 실행

def isPalindrome(s):
    return recursion(s, 0, len(s)-1), cnt

t = int(input())

for i in range(t):
    cnt = 0
    ans, re = isPalindrome(input())
    print(ans, re)