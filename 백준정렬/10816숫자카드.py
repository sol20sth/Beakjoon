import sys
input = sys.stdin.readline

N = int(input())
lisM = list(map(int, input().split()))

dict1 = {}      # 빈 딕셔너리 만들기
for i in lisM:  # lisM의 요소들을 확인
    if i in dict1:  # 상근이 카드가 dict1에 있으면 +1
        dict1[i] += 1
    else:       # 없으면 1
        dict1[i] = 1    
        # dict는 카드 숫자랑 그 숫자의 개수 


M = int(input())
lisN = list(map(int, input().split()))

for i in lisN:      #똑같이 반대로 비교
    if i in dict1:  # 있으면 프린트 줄없이 1칸 띄어서
        print(dict1[i], end=' ')    # 존재하는 숫자 카드라면
    else:
        print(0, end=' ') # 없으면 0 한칸 띄고