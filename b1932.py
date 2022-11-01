# 1932 정수 삼각형

n = int(input())
ans = []
for i in range(n): ## 2차원 입력받음
    ans.append(list(map(int, input().split())))

## 모든 경우를 구해야 함 (ans에 값 누적)
for i in range(1, n):
    for j in range(len(ans[i])):
        if(j==0):
            ans[i][j] = ans[i-1][j] + ans[i][j]
        elif(j==len(ans[i])-1):
            ans[i][j] = ans[i-1][j-1] + ans[i][j]
        else:
            ans[i][j] = max(ans[i-1][j]+ans[i][j], ans[i-1][j-1]+ans[i][j])

print(max(ans[n-1]))