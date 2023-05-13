'''
실패율 == 스테이지 도착 >> 클리어하지 못한 플레이어수 /스테이지에 도달한 플레이어수 
N = 전체 스테이지
stages = 사용자가 현재 멈춰있는 스테이지배열
실패율 높>> 낮은 배열리턴

N 1~500
stacge 1 200000
stage[i] 1~N+1
N+1 클리어
실패율같으면 작은번호 스테이지
도달 x 실패율 0
'''

def solution(N, stages):
    answer = []
    mx = max(stages)
    stack = [0] * (mx+2)
    stack2 = [0] * (mx+2)
    for i in range(len(stages)):
      stack[stages[i]] += 1

    for i in range(len(stack)-2, -1, -1):
      stack2[i] = stack2[i+1] + stack[i]
    
    fail = []
    for i in range(1, N+1):
      fail.append(stack[i]/stack2[i])
    dic = {}
    for i in range(len(fail)-1, -1, -1):
      dic[i+1] = fail[i]
    dicc = sorted(dic.items(), key=lambda x: x[1])
    for i in range(N-1, -1, -1):
      answer.append(dicc[i][0])
    return answer

arr = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, arr))