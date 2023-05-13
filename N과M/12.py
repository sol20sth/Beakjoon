def f(start):
  if len(s) == m:
    print(*s)
    return
  tmp = 0
  for i in range(start, n):
    if tmp != arr[i]:
      # print(s, tmp)
      tmp = arr[i]
      s.append(arr[i])
      f(i)
      s.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
f(0)