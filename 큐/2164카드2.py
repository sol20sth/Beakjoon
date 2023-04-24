import sys
input = sys.stdin.readline
n = int(input())
q = [x for x in range(1, n+1)]  # 1~n까지의 카드
front = 0 # 빼낼 인덱스
rear = 0  # 집어넣을 인덱스 
          # 원형큐를 사용할 건데 원소가 모두 들어가 있는 상태라서 0,0으로 잡음
cnt = n   # 남아있는 숫자카드 개수
while cnt>1:  #남아있는 숫자카드가 1개까지 반복문
  q[front] = 0  # 카드하나뺴고
  cnt -= 1    #숫자뺴고
  front = (front+1) % n   # 프론트 위치 한칸 앞으로
  q[rear] = q[front]    # 카드하나 더뺴서 맨 뒤로 이동
  rear = (rear+1) % n # 맨 뒷칸 이동 == 넣을 곳 이동
  q[front] = 0    # 뺀 곳 0으로 만들기
  front = (front+1) % n # 프론트 한칸 앞으로 
                # 이게 한 사이클
for i in set(q):    # 이 큐에서 0이 아닌것 프린트
  if i != 0:
    print(i)