from itertools import combinations

def solution(info, query):
    answer = []

    info = sorted(list(map(lambda x: x.split(' '), info)), key=lambda x : -int(x[-1]))
    # print(info)

    for i in query:
        a, b, c, d = i.split(' and ')
        d, e = d.strip().split(' ')
        e = int(e)
        li = []
    for i in ['python','cpp', 'java']:
        for j in ['backend', 'frontend']:
            for k in ['junior', 'senior']:
                for l in ['chicken', 'pizza']:
                  li.append([i, j, k, l])
    print(li)
        # answer.append(f(info, [a, b, c, d, e]))
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))