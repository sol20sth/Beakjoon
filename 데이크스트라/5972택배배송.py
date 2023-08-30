import sys

def dsk(start, end):
    if start in clear:
        return 
    else:
        if 


n, m = map(int, input().split())
li = list(map(int, input().split()) for _ in range(m))

farm = [[0] * n for _ in range(n)]

for a, b, c in li:
    farm[a][b], farm[b][a] = c, c
clear, conform = [], []
dsk(0, n-1)

        