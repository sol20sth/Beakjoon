def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(1, n+1):
    if len(s)==0:
      s.append(i)
      f()
      s.pop()
    else:
      if s[-1] <= i:
        s.append(i)
        f()
        s.pop()

n , m = map(int, input().split())
s = []
f()