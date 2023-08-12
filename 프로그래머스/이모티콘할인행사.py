from itertools import product # 중복순열

def solution(users, emoticons):
    answer = []  # 정답리스트
    cases = []   # 이모티콘 퍼센트 케이스들 받을 리스트
    tmp = product([40, 30, 20, 10],repeat=len(emoticons)) # 40, 30, 20, 10 이모티콘 개수 중복순열
    for i in tmp:
        cases.append(i) # 케이스에 넣어주기
    print(cases)
    for case in cases: # 케이스 모두 탐색
        ans = [0, 0]  
        for per, price in users: # 유저정보 하나하나 빼고 비용이랑 퍼센트 확인
            cost = 0
            for i in range(len(emoticons)): 
                if case[i] >= per:   # 유저가 살 퍼센트이면 
                    cost += emoticons[i] * (100 - case[i]) // 100 # 비용 확인 후 더해주기
            if cost >= price:  # 유저가 산 이모티콘 비용 확인 후 유저가 살 비용 이상이면
                ans[0] += 1   # 가입
            else:  # 살 수 있으면
                ans[1] += cost  # 비용에 추가
        answer.append(ans)  # 정답에 가입, 비용 리스트 넣기
    answer.sort(key=lambda x:(-x[0], -x[1])) # 가입 많은 순 비용많은 순으로 정렬 
    return answer[0] # 첫번째 리턴

print(solution([[40, 10000], [25, 10000]],[7000, 9000]))
