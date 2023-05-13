import sys
input = sys.stdin.readline
m,n = map(int, input().split())
num = int(input())
lnm = [0] * (m+1)
lnn = [0] * (n+1)
for i in range(num):
    a, b = map(int, input().split())
    if a == 1:
        lnm[b] = 1
    else:
        lnn[b] = 1
mxm, mxn = 0, 0
mm, nn = 0, 0
for i in range(m+1):
    if lnm[i] == 1 or i == m:
        if mm < mxm:
            mm = mxm
        mxm = 1
    else: 
        mxm += 1
for i in range(n+1):
    if lnn[i] == 1 or i == n:
        if nn < mxn:
            nn = mxn
        mxn = 1
    else: 
        mxn += 1
# print(nn, mm)
print(nn*mm)