# 백준 1700 멀티탭 스케줄링 (그리디)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int,input().split()))

## 1. 멀티탭에 이미 있는 경우 PASS
## 2. 멀티탭에 없고, 멀티탭 자리가 있는 경우 멀티탭에 추가
## 3. 멀티탭에 없고, 멀티탭 자리가 없는 경우?
    # 이후에 또 나온다면...
    # 멀티탭에 있는 것들 중 이후 안나오는 번호 삭제 후 +1
    # 멀티탭에 있는 것들이 전부 이후에 나온다면?
        # 더 적게 나오는 것을 빼기 ++
        # 그중에서도 더 뒤에 나오는 것을 빼기

tap = [] # 멀티탭
ans = 0

while arr:
    now = arr[0]
    ## 2. 멀티탭 자리가 있는 경우 추가
    if len(tap) < n and now not in tap:
        tap.append(now)
        arr.remove(now) # tap에 넣었으니 삭제
        continue

    ## 1. 멀티탭에 이미 있는 경우 PASS
    if now in tap:
        arr.remove(now) # tap에 넣었으니 삭제
        continue
    
    val = 0 ## 인덱스로 사용 (값)
    lastidx = 0 # 가장 나중에 나오는 번호

    for mt in tap: 
        ## 멀티탭에 있는 용품 중 이후에 안나오는 번호가 있으면
        # 해당 번호 빼고 now를 tap에 저장
        if mt not in arr:
            val = mt
            break
        else: # 다 나오는 번호면
            # 그 중 가장 나중에 나오는 번호로 저장
            # print("arr", arr)
            # print("mt", mt, ", arr.index(mt)", arr.index(mt))
            # print("lastidx", lastidx)
            if arr.index(mt) > lastidx:
                lastidx = arr.index(mt)
                val = mt
    # print("-----")
    # print("now", now)
    # print("maxidx", lastidx)
    # print("tap", tap)
    tap[tap.index(val)] = now
    # print("tap", tap)
    # print("-------------------")
    arr.remove(now)
    ans +=1

print(ans)