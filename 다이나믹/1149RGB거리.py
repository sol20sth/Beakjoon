# def f(color, cnt, row):
#     global mi
#     if cnt > mi :
#         return 
#     if row == n:
#         mi = min(mi , cnt)
#         return
#     for i in range(3):
#         if i != color:
#             f(i, cnt+colors[row][i], row+1)

# import sys
# input = sys.stdin.readline
# n = int(input())

# colors = [list(map(int, input().split())) for _ in range(n)]
# mi = 3000 * 1000
# for i in range(3):
#     f(i, colors[0][i], 1)
# print(mi)


n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n):
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))