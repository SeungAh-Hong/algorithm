def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ""
    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
    
    return participant[-1]

## 해시로 풀기
# def solution(participant, completion):
#     dictp = {}
#     sumh = 0
    
#     for part in participant:
#         dictp[hash(part)] = part
#         sumh += hash(part)
    
#     for comp in completion:
#         sumh -= hash(comp)
    
#     return dictp[sumh]
    