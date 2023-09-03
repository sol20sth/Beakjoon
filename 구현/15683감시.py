import sys
import copy
from itertools import product
input = sys.stdin.readline

dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0] # 상 우 하 좌

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
stack = []

for i in range(n):
    for j in range(m):
        if li[i][j] != 0 and li[i][j] != 6:
            stack.append([i, j])
stack2 = []
for y, x in stack:
    if li[y][x] == 1:
        stack2.append([[0], [1], [2], [3]])
    elif li[y][x] == 2:
        stack2.append([[1, 3], [0, 2]])
    elif li[y][x] == 3:
        stack2.append([[0, 1], [1, 2], [2, 3], [3, 0]])
    elif li[y][x] == 4:
        stack2.append([[0, 1, 2], [1, 2, 3], [2,3 , 0], [3, 0, 1]])
    elif li[y][x]== 5:
        stack2.append([[0, 1, 2, 3]])
print(stack, stack2)
stack3 = []
for i in range(len(stack)):
    stack3.append([i for i in range(len(stack2[i]))])
mi = float('inf')
print(stack2, stack3, 'stack3')
for i in list(product(*stack3)):
    li2 = copy.deepcopy(li)
    for j in range(len(stack)):
        y, x = stack[j][0], stack[j][1]
        print(y, x, 'yx')
        tmp = 1
        while True:
            yy, xx = y + tmp*dy[i[j]], x + tmp*dx[i[j]]
            if 0<=yy<n and 0<=xx<m:
                if li2[yy][xx]  == 6:
                    break
                elif li2[yy][xx] == 0:
                    li2[yy][xx] = 7
                    tmp += 1
                else: 
                    tmp+=1
                    continue
            else:
                break
    print(li2)
    mi = min(sum(row.count(0) for row in li2), mi)
print(mi)
# list(product(*stack3))

                    