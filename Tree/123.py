def solution(n, k, reqs):
    counselors = [[] for _ in range(k)]

    reqs.sort(key=lambda x: x[0])
    
    for req in reqs:
        start_time, duration, type = req
        type_counselors = counselors[type]
        min_end_time = float('inf')
        for c in type_counselors:
            if c[1] <= start_time:
                min_end_time = min(min_end_time, c[1] + duration)

        type_counselors.append((start_time, min_end_time))

        type_counselors.sort(key=lambda x: x[0])

        max_end_time = max(type_counselors, key=lambda x: x[1])[1]
        answer = max(answer, max_end_time - start_time)
    
    return answer
