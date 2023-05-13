import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
  num, n = map(int, input().split())
  s = ''
  while num>=n:
    s = str(hex(num%n)[2:]) + s
    num = num // n    
  s = str(hex(num)[2:]) + s
  # print(s)
  print(int(s == s[::-1]))