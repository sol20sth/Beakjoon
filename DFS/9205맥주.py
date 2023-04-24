
def bfs():
    while q: # 방문 할 곳이 있을때까지
        n = q.popleft()  # 하나 뺴내서 현재위치로
        print(n)
        if n == k: # 목표지점 도착하면
            print(visited[n]-1) # 움직인 수 : 초기값을 1로 잡았기때문에 -1해주고 프린트
            cnt = 1
            print(q)
            while q:
                m = q.popleft()
                if m == k and visited[m]==visited[n]:
                    cnt += 1
            return cnt
        for d in [n, -1, 1]: # 현재위치에서 *2, -1, +1 만큼 움직일 수 있는 곳 탐색
            nd = d + n 
            if 0<=nd<mx and visited[nd]==0: # 각각의 값들이 범위내에 있고 방문한 적이 없으면
                visited[nd] = visited[n] + 1 # 방문처리 
                q.append(nd) # nd 값을 움직일 수 있는 값으로 추가
                go[nd] = n # nd 번은 n에서 왔다는 처리

from collections import deque
N, k = map(int, input().split())
mx = 100001  # 최대값 설정
visited = [0] * mx  # 방문처리할 리스트
go = [0] * mx  # 현재위치는 어디에서 이동해서 왔는지 받을 리스트 >> index는 부모 , 값은 자식
visited[N] = 1  # 현재위치 방문처리

q = deque()
q.append(N) # 현재위치 이동가능한 위치에 넣기 > 초기값
print(bfs())

