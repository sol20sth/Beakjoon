def permu():
  if len(s)==n:
    permulist.append(s[::])
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = 1
      s.append(i)
      permu()
      s.pop()
      visited[i] = 0

T = int(input())
for tc in range(T):
  arr = list(map(int, input().split()))
  n = len(arr)
  arr_f = list(map(int, input().split()))
  s = []
  visited = [0] * n
  permulist = []
  permu()
  mx = 0

  for li in permulist:
    print(li)
    ans = 0
    for i in range(len(li)):
      if i != len(li)-1 :
        if arr[i] > 0 and arr[i+1] > 0:
          tmp = min(arr[i], arr[i+1])
          tmp2 = min(li[i], li[i+1])
          ans += arr_f[tmp2]*tmp
          arr[i] = tmp
          arr[i+1] -= tmp
      else:
        if arr[i] > 0 and arr[0] > 0:
          tmp = min(arr[0], arr[i])
          tmp2 = min(li[i], li[0])
          ans += arr_f[tmp2]*tmp
          
          arr[i] = tmp
          arr[0] -= tmp
    mx = max(ans, mx)
  print(mx)