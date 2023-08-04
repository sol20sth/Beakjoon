def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    stack = [0, 0]
    
    for i in range(n):
        stack[0] += deliveries[i]
        stack[1] += pickups[i]

        while stack[0] > 0 or stack[1] > 0:
            stack[0] -= cap
            stack[1] -= cap
            answer += (n - i) * 2

    return answer