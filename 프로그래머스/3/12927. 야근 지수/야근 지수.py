import heapq

def solution(n, works):
    answer = 0
    q = []
    for work in works:
        heapq.heappush(q, (-work, work))

    for _ in range(n):
        tmp, a = heapq.heappop(q)
        a -= 1
        heapq.heappush(q, (-a, a))
    
    for tmp, a in q:
        if a < 0:
            answer = 0
            break
        
        answer += (a*a)
    return answer