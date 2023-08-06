def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1] # 가장 멀리있는 곳부터 방문할 예정
    pickups = pickups[::-1] # 가장 멀리있는 곳부터 방문할 예정
    answer = 0
    stack = [0, 0]  # [배달, 수거]
    
    for i in range(n): 
        stack[0] += deliveries[i]  #방문 후 배달, 수거 값 저장
        stack[1] += pickups[i]

        while stack[0] > 0 or stack[1] > 0:  # 해당 스택의 값이 둘다 0일때까지 방문
            stack[0] -= cap                    # 한번돌때 cap개수만큼 최대로 뺄 수 있음 배달 후 수거 하니까 
            stack[1] -= cap
            answer += (n - i) * 2    # 거리 == n-1 왔다갔다하니까 * 2

    return answer