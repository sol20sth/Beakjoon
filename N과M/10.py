def f(start):
  if len(s) == m:
    print(*s)
    return
  tmp = 0
  for i in range(start, n):
    if visited[i] == 0 and tmp != arr[i]:
      tmp = arr[i]
      visited[i] = 1
      s.append(arr[i])
      f(i)
      visited[i] = 0
      s.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n
s = []
f(0)