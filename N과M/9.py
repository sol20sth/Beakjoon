def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    target = 0
    for i in range(n):
        if not visited[i] and target != arr[i]:
            visited[i] = True
            s.append(arr[i])
            target = arr[i]
            f()
            visited[i] = False
            s.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
s = []
f()