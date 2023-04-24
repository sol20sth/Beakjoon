import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0] * n
for i in range(n):
    t = arr[i]
    while stack and arr[stack[-1]] < t:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1
    stack.append(i)

print(" ".join(list(map(str, ans))))


#####################################

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
mx = 0
mi = 1000000001
for i in range(len(arr)):
    if arr[i] > mx:
        mx = arr[i]
        print(0, end=" ")
    elif arr[i] <= mi:
        mi = arr[i]
        print(i, end=" ")
    else:
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                print(j+1, end=" ")
                break
print()