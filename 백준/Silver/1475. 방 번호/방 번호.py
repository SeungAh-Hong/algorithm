# [1475] 방번호

n = list(map(int, input()))
#print(n)
cnt = [0] * 10
for tmp in n:
    cnt[tmp] += 1

val = (cnt[6] + cnt[9])//2
if (cnt[6]+cnt[9])%2==0:
    cnt[6]=val
    cnt[9]=val
else:
    cnt[6]=val+1
    cnt[9]=val+1

print(max(cnt))

# 반례
# 67890
# answer: 1