def f():
  if len(s) == m:
    print(*s)
    return
  tmp = 0
  for i in range(n):
    if tmp != arr[i]:
      tmp = arr[i]
      s.append(arr[i])
      f()
      s.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
f()