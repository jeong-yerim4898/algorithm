def num(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def oper(x):
    if x=='*' or x=='/':
        return 2
    elif x=='+' or x=='-':
        return 1
    elif x=='(':
        return 0

def calcul(k):
    for i in range(len(k)):
        if num(k[i]):
            stack.append(k[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if k[i] == '+':
                    result =int(num1)+int(num2)
                elif k[i] == '-':
                    result =int(num1) - int(num2)
                elif k[i] == '*':
                    result =int(num1) * int(num2)
                elif k[i] == '/':
                    result =int(num1) // int(num2)
                stack.append(str(result))
            except:
                ans = -1
    return stack[0]


for tc in range(1,11):
    N = int(input())
    exercise = list(input())
    stack = list()
    postfix = ''
    operator = ['*','/','+','-']
    bracket = ['(',')']

    for c in exercise:
        if num(c):
            postfix+=c
        else:
            if not stack and c in operator:
                stack.append(c)
            elif c =='(':
                stack.append(c)
            elif stack and c==')':
                while stack[-1]!='(':
                    postfix+=stack.pop()
                stack.pop()
            elif oper(c)<=oper(stack[-1]):
                postfix+=stack.pop()
                stack.append(c)
            else:
                stack.append(c)
    while stack:
        postfix+=stack.pop()
    calcul(postfix)

    print(f'#{tc} {calcul(postfix)}')