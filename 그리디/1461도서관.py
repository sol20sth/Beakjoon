n, m = map(int, input().split()) # 책의 수 , 한번에 들 수 있는 책의 개수 
post, nega = [], [] # 양수, 음수받을 리스트
li = list(map(int, input().split())) # 책 위치 리스트
for i in li: # 양수 , 음수 리스트에 각각 집어넣기
    if i > 0 :
        post.append(i)
    else:
        nega.append(i)
post.sort() # 절대값이 큰 수대로 정렬
nega.sort(reverse=True)
ans, tmp = 0, 1 # 정답변수, 마지막 처리인지 확인 변수 (1일때 놔두고 끝낸다고 생각)

while True: # 반복문 1번마다 m개의 책을 이동
    if len(post) < m and len(nega) < m : # 양수, 음수 리스트에 모두 m개가 없으면 끝내기
        break
    if tmp == 1: # 마지막 처리하지 않았으면
        if len(post) >= m and len(nega) >= m: # 둘다 m개의 책을 옮길 수 있으면 
            if post[-1] > -nega[-1]: # 뒤의 절대 값이 큰 수부터 옮기는 처리
                ans += post[-1] # 마지막으로 옮기는 위치라고 생각하고 양수리스트 가장 큰 수 정답에 1번더해주기
                tmp += 1
                for _ in range(m): # 가는길에 놔둘 수 있으니 m개의 큰수들을 없애주기
                    post.pop()
            else:  # 위의 처리대로 음수 처리
                ans -= nega[-1]
                tmp += 1
                for _ in range(m):
                    nega.pop()
        elif len(post) < m: # 양수에 m개만큼의 숫자가 없으면 음수에서 마지막 처리
            ans -= nega[-1]
            tmp += 1
            for _ in range(m):
                nega.pop()
        else: # 음수에 m개 만큼의 숫자가 없으면 양수에서 마지막 처리
            ans += post[-1]
            tmp += 1
            for _ in range(m):
                post.pop()
    else:  # 마지막처리를 끝냈으면 
        if len(post) >= m and len(nega) >= m: # 위의 처리와 비슷하지만 0으로 왔다갔다 해야하므로 
            # 정답에 2번 더해주기
            if post[-1] > -nega[-1]:
                ans += post[-1] * 2
                for _ in range(m):
                    post.pop()
            else:
                ans -= nega[-1] * 2
                for _ in range(m):
                    nega.pop()
        elif len(post) < m:
            ans -= nega[-1] * 2
            for _ in range(m):
                nega.pop()
        else:
            ans += post[-1] * 2
            for _ in range(m):
                post.pop()
# 반복문이 끝나고 남아있는 양수 음수 처리 해야함
if tmp == 1:  # 마지막 처리를 안한 상태라면
    if len(post) > 0 and len(nega) > 0: # 음, 양수 모두 빈리스트가 아니라면
        ans += max(post[-1], abs(nega[-1])) # 더 먼거리를 마지막처리해주고
        ans += 2 * min(post[-1], abs(nega[-1])) # 더 가까운 거리를 왔다갔다 하게 만들기
    elif len(post) > 0: # 음수가 비어있다면 양수에서 바로 처리 
        ans += post[-1]
    elif len(nega) > 0: # 양수가 비어있다면 음수에서 바로 처리
        ans -= nega[-1]
else: # 마지막이 아니라면
    # 모두 왔다갔다 생각해서 위의 처리를 모두 왔다갔다 하는 처리
    if len(post) > 0 and len(nega) > 0: 
        ans += 2 * max(post[-1], abs(nega[-1]))
        ans += 2 * min(post[-1], abs(nega[-1]))
    elif len(post) > 0:
        ans += 2 * post[-1]
    elif len(nega) > 0: 
        ans -= 2 * nega[-1]
print(ans)