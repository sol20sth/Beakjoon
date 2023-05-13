import sys
input = sys.stdin.readline

a = input()
b = []
for i in a:
    if i == '(' or i == ')' or i == '[' or i == ']':
        b.append(i)
        
    if (b[0] == ')' or ']') or (b[-1] == '(' or '['):
        print("No")
    elif b.count('(') != b.count(')') or b.count('[') != b.count(']'):
        print("No")
    elif 
