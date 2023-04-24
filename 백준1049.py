import sys
input = sys.stdin.readline

num_line, num_brand = map(int, input().split())
c = num_line % 6
d = num_line // 6
all_p = []
all_v = []
for i in range(num_brand):
    pack, value = map(int, input().split())
    all_p.append(pack)
    all_v.append(value)
    min(all_v)
    
if min(all_p) >= min(all_v)*6:
    print(min(all_v)*num_line)
else:
    if (min(all_v) * c) < min(all_p):
        print(min(all_p)*d + min(all_v)*c)
    else:
        print(min(all_p) * (d+1))
