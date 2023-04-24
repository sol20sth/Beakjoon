a, b = map(int, input().split())
total = 1
c = max(b, a-b)
d = min(b, a-b)
for i in range(c+1, a+1):
  total *= i
for i in range(1, d+1): 
  total = total // i
  
print(total)