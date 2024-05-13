def solution(numbers, target):
    answer = 0
    haps = [0]

    for num in numbers:
        tmp = []
        for hap in haps:
            tmp.append(hap + num)
            tmp.append(hap - num)
        haps = tmp
        
    for hap in haps:
        if hap == target:
            answer += 1
    return answer