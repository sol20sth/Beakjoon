paper_num = int(input())
num_list = []
num_list2 = []
same = []
for i in range(paper_num):
    num_list.append(int(input()))

mini = min(num_list)

if max(num_list)**0.5 < mini:
    for j in range(2, int(max(num_list)**0.5)+1):
        for k in range(paper_num):
            num_list2.append(num_list[k] % j)
        if len(set(num_list2)) == 1:
            same.append(j)
            num_list2=[]
        else:
            num_list2=[]
else:
    for j in range(2, mini+1):
        for k in range(paper_num):
            num_list2.append(num_list[k] % j)
        if len(set(num_list2)) == 1:
            same.append(j)
            num_list2=[]
        else:
            num_list2=[]
# print(same)
for z in same:
    print(f"{z}" ,end =' ')