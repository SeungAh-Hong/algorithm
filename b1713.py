# 1713 후보 추천하기

import sys
input = sys.stdin.readline

N = int(input()) # 사진 틀 개수
M = int(input()) # 전체 학생의 총 추천 횟수
nums = list(map(int, input().split())) # 추천받은 학생 번호 (추천받은 순서)
pictures = [] # 사진 틀
votes = [] # 추천 수

for i in range(M):
    if nums[i] in pictures: # 이미 사진틀에 있는 학생인 경우
        for j in range(len(pictures)):
            if nums[i] == pictures[j]:
                votes[j] += 1
    else: # 사진틀에 없는 학생인 경우
        # 사진틀에 자리가 있는 경우
        if len(pictures) != N:
            pictures.append(nums[i])
            votes.append(1) # 1 추가 (새로운 사진)
        # 사진틀에 자리가 없으면
        else:
            for j in range(N):
                if votes[j] == min(votes): # 가장 작은 점수 삭제
                    del pictures[j]
                    del votes[j]
                    pictures.append(nums[i])
                    votes.append(1) # 1 추가 (새로운 사진)
                    break # 한 개만 삭제

pictures.sort()
for p in pictures:
    print(p, end=' ')
