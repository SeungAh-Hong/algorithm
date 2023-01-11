# 17829 222-풀링

## 23:15 시작 23:30 끝
import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

def pooling(i, j):
    arr = []
    arr.append(matrix[i][j])
    arr.append(matrix[i+1][j])
    arr.append(matrix[i+1][j+1])
    arr.append(matrix[i][j+1])

    arr = sorted(arr) # 2번째로 큰 수 return
    return arr[-2]


while len(matrix) != 1:
    temp = []
    for i in range(0, len(matrix), 2):
        tmp = [] # 리스트 한 줄씩 담아서 temp에 저장할 배열
        for j in range(0, len(matrix), 2):
            tmp.append(pooling(i, j))
        temp.append(list(tmp))

    # print(temp)
    matrix = temp

print(str(*matrix)[1:-1]) ## 대괄호 없이 출력