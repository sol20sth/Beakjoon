N, r, c = map(int, input().split())
# 구간을 4구간으로 나누어서 해당구역보다 작은 구역을 더해준다.
def devi(N, r, c):
    if r < 2**(N-1):
        if c < 2 **(N-1):
            total = 0
        else:
            total = (4**(N-1))
    else:
        if c < 2 **(N-1):
            total =  (4**(N-1)) * 2
        else:
            total = (4**(N-1)) * 3
    return total
sum = 0
# 4구간을 N-1번 나누어 주면 위치가 나옴
for i in range(0,N):

    sum += devi(N-i , r, c)
    r = r % 2**(N-i-1)
    c = c % 2**(N-i-1)
    # print(sum)
print(sum)
    