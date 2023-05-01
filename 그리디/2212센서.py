def f(start, remain, sm, cnt):
  global mi
  if start == len(li) or cnt > m:
    return
  if remain == 1:
    sm += li[-1] - li[start]
    mi = min(mi, sm)
    return
  for i in range(start, len(li)):
    f(i+1, remain-1, sm+li[i]-li[start], cnt+1)

n = int(input())
m = int(input())
li = list(set(map(int, input().split())))
li.sort()
mi = 10000000
f(0, m, 0, 0)
print(mi)
print(li)