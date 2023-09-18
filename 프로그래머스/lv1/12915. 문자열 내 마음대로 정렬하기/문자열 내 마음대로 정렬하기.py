def solution(strings, n):
    answer = []
    strings = sorted(strings, key = lambda x:(x[n:n+1], x))
    
    for st in strings:
        answer.append(st)
        
    return answer