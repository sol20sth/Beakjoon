def f(arr):
    mx = 0
    for i in range(len(arr)):
        if arr[i] > mx:
            mx = arr[i]
        else:
            arr[i] = mx
    return sum(arr)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

bil = [0] * (max(arr)[0]+1)
for i, j in arr:
    bil[i] = j
# print(bil)
# max(bil)
mx , mxidx = 0, 0

for i in range(len(bil)):
    if bil[i] > mx:
        mx = bil[i]
        mxidx = i
left = bil[:mxidx]
right = bil[mxidx+1:][::-1]

print(mx + f(left) + f(right))

