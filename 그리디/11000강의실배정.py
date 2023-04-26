n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
mxtime = 0
for i in range(n):
    mxtime = max(mxtime, room[i][1])
cl = [0] * (mxtime+1)
for i, j in room:
    for x in range(i, j):
        cl[x] += 1
print(max(cl))