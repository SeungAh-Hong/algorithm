str1 = input()
str2 = input()

str_len = max(len(str1), len(str2))
dp = [[0]*(str_len+4) for _ in range(str_len+4)]

# idx 1부터 시작 (앞은 전부 0)
for i in range(len(str2)):
    # str2의 문자 하나당(m) str1 전체(n) 비교
    ## 같은 문자가 나오면 이전 dp+1
    ## 다른 문자가 나오면 왼쪽, 위쪽 dp 비교 후 큰 값 저장
    m = str2[i]
    for j in range(len(str1)):
        n = str1[j]
        if m == n:
            ## 같은 경우 왼쪽 대각선 위의 값 + 1
            dp[i+1][j+1] = dp[i][j] + 1 ## dp는 1,1 부터 채워줌
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        j+=1

## 확인
# for i in range(str_len+2):
#     for j in range(str_len+2):
#         print(dp[i][j], end=' ')
#     print()

print(max(max(dp)))