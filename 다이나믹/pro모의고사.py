def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            cnt1 += 1
        if answers[i] == b[i%8]:
            cnt2 += 1
        if answers[i] == c[i%10]:
            cnt3 += 1
    mx = max(cnt1, cnt2, cnt3)
    if cnt1 == mx:
        answer.append(1)
    if cnt2 == mx:
        answer.append(2)
    if cnt3 == mx:
        answer.append(3)

    return answer



12345
21232425
31245*2