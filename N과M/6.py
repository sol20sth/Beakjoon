def f(end):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(end, n):
    if arr[i] not in s:
      s.append(arr[i])
      f(i)
      s.pop()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
f(0)