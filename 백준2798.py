N, M = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if(num[i] + num[j] + num[k] > M):
                continue
            else:
                ans = max(ans ,num[i] + num[j] + num[k])

print(ans)