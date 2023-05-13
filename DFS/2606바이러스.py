import sys
input = sys.stdin.readline

def dfs(start):     # 깊이 탐색
    global cnt      # 재귀함수를 쓰기 때문에 고정된 하나의 cnt 부르기
    visited[start] = 1  # 방문하면 1
    cnt += 1        # 방문하면 횟수+1
    for w in adj[start]:    # start가 방문할 수 있는 곳들 == w 탐색
        if visited[w] == 1:     # 방문한 곳이 예전에 방문 한 곳이면 되돌아가기
            continue
        dfs(w)  # 예전에 방문한 곳이 아니면 w로 다시 dfs호출
    return cnt  # 함수가 끝나면 cnt리턴


T = int(input())
n = int(input())
cnt = 0
visited = [0] * (T+1)       # 방문한 곳들을 체크할 리스트
adj = [[] for _ in range(T+1)]  # 각각의 숫자들이 방문할 수 있는 곳들 저장 할 리스트
for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)    # a 행에 b를 추가 >>> a는 b를 갈 수 있다. 
    adj[b].append(a)    # 반대도 갈 수 있음

print(dfs(1)-1) # 카운드는 본인 포함이니까 본인 빼야해서 -1
    

import sys
input = sys.stdin.readline
def dfs(s):
    global cnt

    stack = []
    visited[s] = 1
    while True:
        for w in adj_lst[s]:
            if visited[w] == 0:
                stack.append(s)  # 
                s = w
                visited[w] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    for x in range(v + 1):
        cnt += visited[x]
        # print(visited)
    return 


v = int(input())
e = int(input())

adj_lst = [[] for _ in range(v + 1)]

for i in range(e):
    start, to = map(int, input().split())
    adj_lst[start].append(to)
    adj_lst[to].append(start)

cnt = 0
visited = [0] * (v + 1)
dfs(1)
print(cnt-1)