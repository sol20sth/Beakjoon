import sys
input = sys.stdin.readline


T = int(input())
words = [0]*T
for i in range(T):
    words[i] = input().rstrip()
words = list(set(words))
words.sort()
words.sort(key=len)
for j in words:
    print(j)