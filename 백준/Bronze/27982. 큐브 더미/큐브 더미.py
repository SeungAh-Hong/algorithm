# [27982] 큐브 더미 
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

cubemap =  [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    cubemap[i-1][j-1][k-1] = 1

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if cubemap[i][j][k] == 1:
                if 0 < i < n-1 and 0 < j < n-1 and 0 < k < n-1:
                    if cubemap[i+1][j][k] == 1 and cubemap[i][j+1][k] == 1 and cubemap[i][j][k+1] == 1:
                        if cubemap[i-1][j][k] == 1 and cubemap[i][j-1][k] == 1 and cubemap[i][j][k-1] == 1:
                            count+=1
print(count)