def f(arr, r):
    for i in range(len(arr)):
        if r == 1:
            return [arr[i]]
        else:
            for j in f(arr[i+1:], r-1):
                return [arr[i]] + j


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
peo = []
for i in range(n):
    peo.append(i)



stack = []
for comb in f(peo, n//2):
    tmp = 0
    for comb2 in f(comb, 2):
        tmp += arr[comb2[0]][comb2[1]] + arr[comb2[1]][comb2[0]]
    stack.append(tmp)


ans = abs(stack[0] - stack[-1])
for i in range(len(stack)//2):
    ans = min(ans, abs(stack[i] - stack[-i-1]))

print(ans)