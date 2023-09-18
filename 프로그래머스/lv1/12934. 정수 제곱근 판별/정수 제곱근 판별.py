import math
def solution(n):
    if n % math.sqrt(n) == 0:
        return math.pow(math.sqrt(n)+1, 2)
    else:
        return -1