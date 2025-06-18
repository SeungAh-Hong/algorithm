import math

def solution(brown, yellow):
    answer = []
    area = brown + yellow
    #w, h = 0, 0
    #area = w * h
    #yellow = (w - 2) * (h - 2)
    
    for h in range(3, area):
        w = area // h
        if (w-2) * (h-2) == yellow:
            answer.append(w)
            answer.append(h)
            return answer
