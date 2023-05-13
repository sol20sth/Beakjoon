house, wifi = map(int,input().split())
house1 = []
for _ in range(house):
    x = int(input())
    house1.append(x)
house1.sort()
start = 1
end = house1[-1] - house1[0]
result = 0

while (start <= end):
    first = house1[0]
    mid = (start+end)//2 
    count = 1
    for i in range(1, len(house1)):
        if house1[i] >= first+mid:
            count+=1
            first = house1[i]   
    if count >= wifi:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)