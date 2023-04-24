T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    mi = 10000000
    TF = 0
    arr.sort()
    for i in range(1,n-1):
        if arr[i-1] == arr[i]:
            continue
        for j in range(i+1, n):
            if arr[j-1] == arr[j]:
                continue
            cnt1, cnt2, cnt3 = i, j-i, n-j
            # print(cnt1, cnt2, cnt3)
            if cnt1<=n//2 and cnt2<=n//2 and cnt3<=n//2:
                mi = min(mi, (max(cnt1, cnt2, cnt3) - min(cnt1, cnt2, cnt3)))
                TF = 1
    if TF == 1:
        print(f'#{tc} {mi}')
    else:
        print(f'#{tc} -1')