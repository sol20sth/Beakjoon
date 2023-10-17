import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
sm = sum(li) # 전체 꿀의 양
tmp, tmp2 = li[0], li[-1]
answer = 0
# 벌벌꿀인,꿀벌벌인
for i in range(1, n): 
    # 왼쪽끝에 벌 하나 고정, 꿀단지 오른쪽에 고정 >> 벌하나만 그사이에서 이동하며 최대값 비교
    tmp += li[i]  # 변경하고 있는 벌이 이동(먹지)못하는 꿀 양
    answer = max(answer, sm - li[0] + sm - tmp - li[i])  # sm - li[0](본인 꿀) == 왼쪽 끝의 벌의 꿀  , sm - tmp -li[i](본인 꿀)
    # 오른쪽끝에 벌 하나 고정, 꿀단지 왼쪽에 고정 >> 벌하나만 그사이에서 이동하며 최대값 비교
    tmp2 += li[n-1-i]
    answer = max(answer, sm - li[-1] + sm - tmp2 - li[n-1-i])

# 벌꿀벌
for i in range(1, n):
    answer = max(answer, sm - li[0] - li[-1] + li[i]) # 본인 위치 꿀을 제외한 모든 꿀은 탐색가능 하지만 꿀통은 2번 먹음

print(answer)