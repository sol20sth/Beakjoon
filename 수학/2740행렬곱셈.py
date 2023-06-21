n, m = map(int, input().split())
li1, li2 = [], []
for i in range(n):
    li1.append(list(map(int, input().split())))  # n * m 행렬
m, k = map(int, input().split())
for i in range(m):
    li2.append(list(map(int, input().split()))) # m * k 행렬

ans = [[0] * k for _ in range(n)] # 두개를 곱하면 n * k 행렬
for i in range(n): # 행 == n
    for j in range(k): # 열 == k
        for l in range(m): # 한 칸마다 m번 곱
            ans[i][j] += li1[i][l] * li2[l][j]

for i in range(n):
    print(*ans[i])