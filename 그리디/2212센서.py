n = int(input())
m = int(input())
li = list(map(int, input().split()))
li.sort()
dis = []
if n >= m:
  for i in range(n-1):
      dis.append(li[i+1] - li[i])
  dis.sort()
  for _ in range(m-1):
      dis.pop()
  print(sum(dis))
else:
  print(0)