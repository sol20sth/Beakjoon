n, k = map(int, input().split())
container = list(map(int, input().split()))

line_num = 0
z_count = container.count(0)
robot = [0] * (2*n)
ans = 0
while z_count < k:
    ans += 1
    line_num = (line_num - 1) % (2*n)
    for i in range(n, 0, -1): 
        if i == n-1:
            robot[(line_num+i)%(2*n)] = 0
            continue
        print(robot)
        print(container)
        if container[(line_num+i+1)%(2*n)] != 0 and robot[(line_num+i)%(2*n)] != 0 and robot[(line_num+i)%(2*n)] == 0:
            robot[(line_num+i+1)%(2*n)] = 1
            robot[(line_num+i)%(2*n)] = 0
            container[(line_num+i+1)%(2*n)] -= 1
            print('아아아앙')
    if container[line_num] != 0:
        robot[line_num] = 1
        container[line_num] -= 1
    z_count = container.count(0)
print(ans)



from collections import deque 

# input 
N, K = map(int, input().split(" "))
belt = list(map(int, input().split(" ")))
belt_length = N*2 -1

queue = deque()
for i in belt:
  queue.append([i, False])

result = 0
while True:
  last = queue.pop()
  queue.appendleft(last)
  queue[N-1][1] = False 
  for i in range(N-2,-1,-1):
    now = queue[i]
    if now[1]:
      next_index = i + 1 
      if queue[next_index][0] > 0 and queue[next_index][1] == False:
        queue[next_index][0] -= 1
        queue[i][1] = False
        queue[next_index][1] = True
        if i == N -2:
          queue[next_index][1] = False
  if queue[0][0] > 0 and queue[0][1] == False:
    queue[0][0] -= 1
    queue[0][1] = True
  broken = 0
  for i in queue:
    if i[0] ==0:
      broken+=1 
  result +=1 
  if broken >= K:
    print(result)
    break