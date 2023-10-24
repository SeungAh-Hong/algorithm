def solution(nums):
    n = len(nums)//2
    set_nums = set(nums)
    m = len(set_nums)
    
    if m >= n:
        answer = n
    else:
        answer = m

    return answer