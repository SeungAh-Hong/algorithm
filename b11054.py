## 백준 11054. 가장 긴 바이토닉 부분 수열 (골드4)

# DP 사용
n = int(input())
A = list(map(int, input().split()))

# 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력
## 증가 수열 + 감소 수열 합이 가장 큰 경우

## dp (O(N^2)), 해당 위치까지의 LIS만 구해서 길이 저장
in_A = [0]*(n+2)
re_A = [0]*(n+2)

for i in range(n):
     in_A[i] = 1
     for j in range(i):
          if A[j] < A[i]:
               in_A[i] = max(in_A[i], in_A[j]+1) ## dp


## 반대로 또 저장
for i in reversed(range(n)):
     re_A[i] = 1
     for j in range(n-1, i, -1):
          if A[j] < A[i]:
               re_A[i] = max(re_A[i], re_A[j]+1)

answer = 0
for i in range(n):
     answer = max(answer, in_A[i] + re_A[i] - 1)

print(answer)


