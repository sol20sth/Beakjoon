'''
촌수 
부모자식간 관계 >> 이차원배열로 각 자식들 표현
n = 전체 사람수 
target = a, b
관계수 N
y, x : 부모 자식
'''

def bfs(a,b):
  q = []      # 빈 큐
  q.append(a) # 현재자리 넣기
  visited = [0]*(n+1)   # 방문체크
  visited[a] = 1    # 현재위치 방문체크
  while q:    # 큐가 빌때까지 반복
    a = q.pop(0)    # 큐에서 첫번째 수 빼서 현재자리로
    for i in arr[a]:  # 현재자리에서 갈 수 있는 자리들 빼내기
      if visited[i] == 0: # 방문한 적 ㅇ벗으면 
        q.append(i)   # 큐에 넣고
        visited[i] = visited[a] + 1   # 방문 체크 +1
        if i == b:    # 만약 i가 목표 사람이면 
          return visited[i]-1   # -1해서 빼내기
  return -1   # 관계없는 사람이면 -1리턴
    

import sys
input = sys.stdin.readline

n = int(input())    # 전체 사람수
a, b = map(int, input().split())  # 촌수 구할 두사람
N = int(input())    # 관계입력 갯수
arr = [[] for _ in range(n+1)]  # 관계 리스트
for i in range(N):  # 관계리스트에 관계있는 사람들 넣기
  y, x = map(int, input().split())
  arr[y].append(x)
  arr[x].append(y)
print(bfs(a,b))