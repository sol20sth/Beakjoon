def solution(n, edges):
    answer = 0
    li = [[0 for _ in range(n)] for _ in range(n)]
    
    print(edges)
    for edge in edges:
        if (edge[0] != edge[1]) and not li[edge[0]-1][edge[1]-1]:
          li[edge[0]-1][edge[1]-1], li[edge[1]-1][edge[0]-1] = 1, 1

    node = [20001 for _ in range(n)]
    node[0] = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                node[j] = min(node[i] + 1 , node[j])
    print(node)
    mx = max(node)
    for i in node:
        if i == mx:
            answer += 1
    return answer

print(solution(7, [[3, 4], [4, 3], [3, 4], [1, 3], [1, 2], [2, 4], [5, 2]]))