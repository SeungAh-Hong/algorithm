## 백준 11054. 가장 긴 바이토닉 부분 수열 (골드4)
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

# 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력
## 증가 수열 + 감소 수열 합이 가장 큰 경우

in_A = [A[0], ]
## 증가 수열의 부분 수열 구함 (in_A에 저장)
for i in range(1, n):
     # 현재 들어온 수가 in_A의 마지막 수보다 작으면 끝 수 자리에 현재 들어온 수 넣어주고,
     # 현재 들어온 수가 마지막 수보다 크면 끝에 넣어줌
     if in_A[-1] < A[i]:
          in_A.append(A[i])
     elif in_A[-1] > A[i]:
          idx = bisect_left(in_A, A[i])
          in_A[idx] = A[i]
     else:
          continue

print(len(in_A))

     # if in_A[-1] > A[i]:
     #      if A[i] in in_A:
     #            ## in_A 배열에 있는 수면 추가 X
     #           continue
     #      else:
     #           # print("현재 수가 작음, in_A:", in_A[-1], "A", A[i])
     #           del in_A[-1]
     #           in_A.append(A[i])
     #           # print(in_A)

     # else:
     #      continue