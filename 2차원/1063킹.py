

dic = {'R':(0, 1), 'L':(0, -1), 'B':(-1,0),'T':(1,0),'RT':(1,1),'LT':(1,-1),'RB':(-1,1),'LB':(-1,-1)}

now , target, num = map(str, input().split())
now = [int(now[1]),ord(now[0])-65]
target = (int(target[1])-1,ord(target[0])-65)

go = [input() for _ in range(int(num))]
y, x = now[0]-1, now[1]

for i in go:
    (dy, dx) = dic[i]
    yy = dy + y 
    xx = dx + x

    if 0<=yy<8 and 0<=xx<8 and (yy,xx) != target:
        y, x = yy, xx
    elif (yy,xx) == target:
        if 0<=yy+dy<8 and 0<=xx+dx<8:
            y, x = yy, xx
            target=(yy+dy,xx+dx)
        else:
            continue
    else:
        continue
print(f'{chr(x+65)}{y+1}')
print(f'{chr(target[1]+65)}{target[0]+1}')


