def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(n):
    s.append(arr[i])
    f()
    s.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
f()