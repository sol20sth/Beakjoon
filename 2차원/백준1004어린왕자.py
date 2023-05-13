T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for j in range(n):
        x3,y3,r = map(int, input().split())
        far1 = (x1-x3)**2 + (y1-y3)**2
        far2 = (x2-x3)**2 + (y2-y3)**2
        if far1 < r**2 and far2 < r**2:
            pass
        elif far1 > r**2 and far2 > r**2:
            pass
        else:
            count += 1
    print(count)