import sys

T = int(input())
total = ''
for i in range(T):
    a, b = map(str, sys.stdin.readline().split())
    for j in range(len(b)):
        total = int(a)*b[j]
print(total)