import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

mx = max(arr)
total = mx * (n-2) + sum(arr)
print(total)