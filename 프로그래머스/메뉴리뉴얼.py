from itertools import combinations
def solution(orders, course):
    answer = []
    # orders에 들어있는 각각의 주문을 정렬시켜서 리스트로 만들기
    orders = list(map(lambda order: sorted(order), orders))
    for i in course:  # 각코스의 메뉴개수별로 탐색
        dic = {}  # 딕셔너리
        mx = 0   # 몇명이 주문했는지 최대값 변수
        for order in orders:  # 각 주문 모두 탐색
            for comb in combinations(order, i):  # 각주문에서 메뉴개수 조합 구해서 모두 탐색
                key="".join(comb)  # 조합은 ()형태로 나오기 때문에 하나의 문자열로 만들기
                if key in dic.keys():  # key가 dic의 key에 있으면 값을 +1
                    dic[key] += 1
                else:  # 없으면 1로 설정
                    dic[key] = 1
                mx = max(mx, dic[key])  # 최대로 시킨 숫자 저장

        if mx >= 2:  # 최대로 시킨 숫자가 2이상일때만 저장
            for i in dic:  # dic 탐색해서 최대로 주문한 숫자이면 key를 answer에 넣어주기
                if mx == dic[i]:
                    answer.append(i)
    answer.sort()
    return answer
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
