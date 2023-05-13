import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    list_p = [list(map(int, input().split())) for _ in range(n)]
    list_p.sort(key=lambda x: x[0])
    cnt = [0] * n
    for i in range(n):
        cnt[i] = n -i -1
        for j in range(i+1, T):
            if list_p[i][1] < list_p[j][1]:
                cnt[i] -= 1
    print(cnt)
    print(max(cnt))