import sys
input = sys.stdin.readline

p, m = map(int, input().split())
dic, dic2 ,stack= {} , {}, []
for _ in range(p):
  tmp = 0
  l, n = map(str, input().split())
  dic2[n] = l
  l = int(l)
  tf = True
  if len(dic.keys())==0:
    dic[l] = [n]
  else:
    for i in dic.keys():
      if i-10<=l<=i+10 and len(dic[i]) != m:
        dic[i].append(n)
        tf = True
        break
  
      elif not i-10<=l<=i+10:
        tf = False
        continue

          
      elif len(dic[i]) == m :
        tf = False
        continue
      
    if tf == False:
      dic[l] = [n]
  
for i in dic.values():
  tmp = sorted(i)
  if len(i) != m:
    print('Waiting!')
  else:
    print('Strated!')

  for z in tmp:
    print(dic2[z], end=" ")
    print(z)