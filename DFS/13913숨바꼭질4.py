def path(x): # 마지막 도착지점에서 계속 방문한곳들 탐색하기 위해
    arr = [] # 방문한 곳들 저장할 리스트
    temp = x # 임시변수
    for _ in range(visited[x]): # 움직인 수 + 1번만큼 탐색 
        # 움직인수는 visited[x] -1 인데 초기값도 뽑아내야 하기떄문에 visited[x]
        arr.append(temp) # 현재 부모노드를 방문한 곳에 추가
        temp = go[temp] # 자식 = go[부모] 이기 떄문에 재설정 후 반복문 계속 
    print(' '.join(map(str, arr[::-1]))) # 목표지점부터 리스트의 왼쪽에 담겼기 떄문에 arr[::-1]
    
def bfs():
    while q: # 방문 할 곳이 있을때까지
        n = q.popleft()  # 하나 뺴내서 현재위치로
        if n == k: # 목표지점 도착하면
            print(visited[n]-1) # 움직인 수 : 초기값을 1로 잡았기때문에 -1해주고 프린트
            path(n) # 목표지점부터 자식을 찾아서 계속 탐색하는 함수
            return 
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
bfs()














# def bfs():
#     while q:
#         n = q.popleft()
#         print(n)
#         if n == k:
#             print(visited[n]-1)
#             print(visitedd[n])
#             return 
#         if n > max(N, k) * 2:
#             continue

#         if 0<=n*2<mx and visited[n*2]==0:
#             visited[n*2] = visited[n] + 1
#             visitedd[n*2] = visitedd[n] + f' {n*2}'
#             q.append(n*2)

#         if 0<=n-1 and visited[n-1]==0:
#             visited[n-1] = visited[n] + 1
#             q.append(n-1)
#             visitedd[n-1] = visitedd[n] + f' {n-1}'


#         if 0<=n+1<mx and visited[n+1]==0:
#             visited[n+1] = visited[n] + 1
#             q.append(n+1)
#             visitedd[n+1] = visitedd[n] + f' {n+1}'



# from collections import deque
# N, k = map(int, input().split())
# mx = 100001
# visited = [[0] for _ in range(mx)]
# visitedd = ['' for _ in range(mx)]
# visited[N] = 1
# visitedd[N] = f'{N}'
# q = deque()
# q.append(N)
# bfs()

