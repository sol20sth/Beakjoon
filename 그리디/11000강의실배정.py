import heapq
import sys
input = sys.stdin.readline
n = int(input()) # 강의 개수
startEnd = [list(map(int, input().split())) for _ in range(n)]
# 강의 시작 끝 시간 리스트
startEnd.sort() # 강의 시작시간을 기준으로 정렬
q = [] # 빈 리스트
heapq.heappush(q, startEnd[0][1]) # q에 가장 먼저시작한 강의의 끝나는 시간 추가
for i in range(1, n): # 리스트 1index 부터 탐색
    if startEnd[i][0] >= q[0]:
        # 만약 강의 시작시간이 q[0] 보다 크거나 같으면 ==> 강의 시간이 겹치지 않으면
        # 더이상 q[0]는 강의 겹치는게 없다고 생각하고 없애주기 
        heapq.heappop(q)
    # 그 후 강의들의 끝나는 시간들을 추가
    heapq.heappush(q, startEnd[i][1])
    # 만약 강의시간이 겹친다면 강의실 추가만 해주기
print(len(q))