import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sky = [input() for _ in range(n)]
for i in range(n):
  cnt , cl = 0, 0
  for j in range(m):
    if cl == 0:
      if sky[i][j] == '.':
        print('-1', end=" ")
      else:
        cl = 1
        cnt = 0
        print('0', end=" ")
    else:
      if sky[i][j] == 'c':
        cl = 1
        cnt = 0
        print('0', end=" ")
      else:
        cnt += 1
        print(f'{cnt}', end=" ")
  print()
