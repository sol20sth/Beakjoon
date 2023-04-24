def f(target):
    global ans
    arr = arr0[:]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != target:

                for dy, dx in [(-1, 0), (1, 0),(0,1),(0,-1)]:
                    yy = dy + i
                    xx = dx + j
                    if 0<=yy<n and 0<=xx<n and arr[yy][xx] == target:
                        arr[i][j] = target
    print(arr)
    print(arr0)
    for i in range(n):
        cnt,mx = 1, 1
        for j in range(1,n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
                if mx > cnt:
                    mx = cnt
            else:
                cnt = 0
        if ans < mx:
            ans = mx
            return
    for i in range(n):
        cnt,mx = 1, 1
        for j in range(1,n):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
                if mx > cnt:
                    mx = cnt
            else:
                cnt = 0
        if ans < mx:
            ans = mx
            return





n = int(input())
arr0 = [list(input()) for _ in range(n)]
ans = 0
sign = ['C','P','Z','Y']
for i in sign:
    f(i)

print(ans)
