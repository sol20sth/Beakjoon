a = list(input())
stack = []
for i in range(len(a)):
    if len(stack) == 0 :
        stack.append(a[i])
    else:
        if a[i] == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            elif stack[-1] == '[':
                stack.append(')')
            else:
                x =len(stack)
                tmp = 0
                tf = True
                for _ in range(x):
                    if type(stack[-1]) == int:
                        tmp += stack[-1]
                        stack.pop()
                        continue
                    if stack[-1] == '(':
                        stack.pop()
                        tf = False
                        break
                if tf == True:
                    stack.append(tmp)
                    stack.append(')')
                else:
                    stack.append(tmp * 2)
        elif a[i] == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            elif stack[-1] == '(':
                stack.append(']')
            else:
                x=len(stack)
                tmp = 0
                tf = True
                for _ in range(x):
                    if type(stack[-1]) == int:
                        tmp += stack[-1]
                        stack.pop()
                        continue
                    if stack[-1] == '[':
                        stack.pop()
                        tf = False
                        break
                if tf == True:
                    stack.append(tmp)
                    stack.append(']')
                else:
                    stack.append(tmp * 3)
        else:
            stack.append(a[i])
if '(' in stack or ')' in stack or '[' in stack or ']' in stack:
    print(0)
else:
    print(sum(stack))