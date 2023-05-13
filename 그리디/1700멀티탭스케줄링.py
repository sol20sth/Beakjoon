'''
한개의 멀티탭
전기용품의 사용순서>>> 플러그 뺴는 횟수 최소화
'''

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# stack, stack2 = [], [0] * (k+1)
# cnt = 0
# for i in arr:
#   stack2[i] += 1


# for i in range(k):
#   stack2[arr[i]] -= 1
#   if arr[i] in stack:
#     continue
#   elif len(stack) == n:
#     mi = 100000
#     cnt += 1
#     for k in range(len(stack)):
#       if stack2[stack[k]] < mi:
#         mi = min(stack2[stack[k]], mi)
#         tmp = k

#     stack.pop(tmp)
#     stack.append(arr[i])

#   elif len(stack) < n:
#     stack.append(arr[i])

# print(cnt)

##########################
n, k = map(int, input().split())
items = list(map(int, input().split()))
tap = []
ans = 0

for i, item in enumerate(items):
    if item in tap:
        continue
    if len(tap) < n:
        tap.append(item)
    else:
        val = 0
        idx = -1
        ans += 1
        tmp = items[i:]
        for x in tap:
          if x in tmp:
            target = tmp.index(x)
            if idx < target:
                idx = target
                val = x
          else:
              val = x
              break
        tap[tap.index(val)] = item

print(ans)
