def solution(array, commands):
    answer = []
    for comm in commands:
        i, j, k = comm
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])

    return answer