# 백준 12873 기념품 (구현)

N = int(input())
nums = []
for i in range(1, N+1):
    nums.append(i)

d = 0
idx = 0
# 지우고나서 그 다음 번째 사람부터 다시 도니까 idx 값 변경해주기!
while len(nums) != 1:
    #print(nums)
    d += 1
    x = pow(d, 3)
    idx = (idx + x) % len(nums)
    if idx == 0:
        del nums[-1]
    else:
        del nums[idx-1]
        idx -= 1
    
    #print("d",d,"x",x,"idx",idx, "num", nums)

print(nums[0])
