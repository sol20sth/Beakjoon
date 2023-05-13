n = int(input())
arr = [x for x in range(1,n+1)]
cnt = 0
for i in range(1, n+1):
  for j in range(i, n+1):
    if i * j > n:
      break
    else:
      cnt += 1
print(cnt)