def dfs(x):
    global cnt
    stack = []
    visited = [0] * (n+1)
    visited[x] = 1
    while True:
        for z in range(n+1):
            if visited[z] == 0 and adj[x][z] == 1:
                stack.append(x)
                x = z
                cnt += 1
                visited[z] = 1
                break
        else:
            if stack:
                x = stack.pop()
            else:
                return cnt

n, m = map(int, input().split())
adj = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
x, y = map(int, input().split())
adj[x][y], adj[y][x] = 1, 1
for i in range(m-1):
    a, b = map(int, input().split())
    adj[a][b], adj[a][b] = 1, 1
cnt = sum(adj[a]) + sum(adj[b]) - 2
print(cnt)


    






