def solution(fees, records):
    answer = []
    car = {}
    stack =[]
    for record in records:
        time, num, inout = map(str, record.split(" ")) 
        time1 , time2 = map(str, time.split(":"))
        if inout == "IN":
            if num not in car:
                car[num] = [time1, time2, "IN", 0]
            else:
                car[num] = [time1, time2, "IN", int(car[num][3])]
        else:
            tmp = (int(time1) - int(car[num][0]))*60 + (int(time2)-int(car[num][1]))
            car[num] = [0, 0, "OUT", car[num][3] + tmp]

    car = sorted(car.items())
    for i in car:
        if i[1][2] == "OUT":
            stack.append(i[1][3])
            continue
        else:
            tmp = (23 - int(i[1][0])) * 60 + (59 - int(i[1][1]))
            i[1][3] += tmp
            stack.append(i[1][3])

    for i in stack:
        if i - fees[0] <= 0:
            answer.append(fees[1])
            continue
        tmp = i -fees[0]
        tmp2 = fees[1]
        if tmp % fees[2] == 0:
            tmp2 += tmp // fees[2] * fees[3]
            answer.append(tmp2)
        else:
            tmp2 += (tmp // fees[2] +1) * fees[3]
            answer.append(tmp2)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))