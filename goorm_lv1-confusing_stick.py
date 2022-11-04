## 구름 난이도 1 - 헷갈리는 작대기
## 경희대학교 기출문제

s = input()
s_list = [char for char in s]
ans = [0, 0, 0, 0]

for i in s_list:
    if(i == '1'):
        ans[0] += 1
    elif(i == 'I'):
        ans[1] += 1
    elif(i == 'l'):
        ans[2] += 1
    elif(i == '|'):
        ans[3] += 1

for i in range(4):
    print(ans[i])