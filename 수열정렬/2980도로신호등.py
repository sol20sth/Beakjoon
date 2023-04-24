import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
al = [0] * (L+1)
now, time = 0, 0
while now != L:
  for i in arr:
    if (time+1) % sum(i[1:]) in range(i[1]):
      al[i[0]] = 1
    else:
      al[i[0]] = 0
  # print(al)
  if al[now+1] == 0:
    now += 1
    time += 1
  else:
    time += 1
print(time)