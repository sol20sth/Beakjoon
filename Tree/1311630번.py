import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    while True:
        if a == b:
            print(a*10)
            break
        elif a<b:
            b = b//2
        else:
            a = a//2