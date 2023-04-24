
import sys
input = sys.stdin.readline
a = []
T = int(input())
for i in range(T):
    b = int(input())
    a.append(b)
a.sort()
for j in a:
    print(j)
    