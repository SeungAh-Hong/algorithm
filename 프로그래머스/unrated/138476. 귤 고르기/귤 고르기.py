from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    sorted_count = count.most_common()
    for gram, cnt in sorted_count:
        if k > 0:
            k -= cnt
            answer += 1

    return answer