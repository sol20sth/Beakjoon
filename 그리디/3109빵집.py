def find(v): # 부모 노드 찾는 함수
    if parent[v] == v: # 자신이면 리턴
        return v
    parent[v] = find(parent[v]) # 재귀로 가장 상위 노드 찾기
    return parent[v] # 함수를 실행했을 때 해당 노드의 최상단 부모노드 찾아짐

def union(a, b): # a, b의 부모노드들을 찾아서 연결
    a = find(a)
    b = find(b)
    parent[b] = a

import sys
input = sys.stdin.readline

g ,p = int(input()), int(input()) # 게이트 수, 비행기 수
parent = [i for i in range(g+1)] # 정착 가능 게이트 
arr = [int(input()) for _ in range(p)]
ans = 0  # 정답 변수
for i in arr: # gi 들을 앞에서부터 꺼내어서 부모노드들을 비교
    P = find(i) # 부모노드 찾기
    if P == 0: # 부모노드가 0이면 게이트가 꽉차있는 것 
        break # 끝내기
    ans += 1  # 꽉차있지 않다면 주차 가능 비행기 개수 +1
    union(P-1, P)  # 해당 비행기의 부모노드와 해당 비행기의 부모노드 -1을 연결

print(ans)