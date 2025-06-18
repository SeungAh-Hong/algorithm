def solution(n, times):
    answer = 0
    times.sort()
    start = times[0]
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for t in times:
            tmp += mid // t
        if tmp >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
            
        
    return answer