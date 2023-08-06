from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1) # pop(0)는 시간이 많이 걸리므로 deque이용
    queue2 = deque(queue2)
    answer = 0  # 정답변수
    cir = 0		# while문 돈 횟수
    tf = 0      # -1 인지 아닌지 확인할 변수
    sm1= sum(queue1)   
    sm2 = sum(queue2)
    ln = len(queue1) + len(queue2)+3  # -1인지 아닌지 확인할 최댓값
    # 최대개수는 [], [] 둘중하나의 -2번째의 자리에 본인을 제외한 모든 값을 합한 숫자를 가지는 경우이므로 +3
    while cir < ln: # 최대 비교횟수가 while문 돈 횟수보다 작을때
        if sm1 < sm2:  # queue2의 합이 크다면
            tmp = queue2.popleft()  # queue2에서 빼고 queue1에 넣기 
            queue1.append(tmp)
            answer += 1
            sm1 += tmp   # 합도 재설정
            sm2 -= tmp
        elif sm1 > sm2:   # 반대의 경우도 똑같이
            tmp = queue1.popleft()
            queue2.append(tmp)
            answer += 1
            sm1 -= tmp
            sm2 += tmp
        else:		# 같을때 
            tf = 1   # -1아니라고 확인 후 끝내기
            break
        cir += 1  # 한번돌때마다 while문 돈 횟수 +1
    if tf == 0:   # 최대로 돌아도 0이면 -1출력
        answer = -1
    return answer