n, k = map(int, input().split())
arr = [x for x in range(1, n+1)]
front = 0
print('<', end="")
while arr:
    front = (front+k-1) % n
    print(f'{arr.pop(front)}', end="")
    n = n-1
    if not arr:
        break
    print(',', end=" ")
print('>', end="")