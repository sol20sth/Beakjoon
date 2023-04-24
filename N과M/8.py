def f(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(start, n):
    s.append(arr[i])
    f(i)
    s.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
f(0)