T= int(input())
for tc in range(1,T+1):
    forth = list(input().split())
    stack=list()
    n=len(forth)
    ans = 0
    for i in range(n-1):
        if forth[i].isdigit():
            stack.append(forth[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if forth[i] == '+':
                    result =int(num1)+int(num2)
                elif forth[i] == '-':
                    result =int(num1) - int(num2)
                elif forth[i] == '*':
                    result =int(num1) * int(num2)
                elif forth[i] == '/':
                    result =int(num1) // int(num2)
                stack.append(str(result))
            except:
                ans = -1

    if ans==0 and len(stack)==1:
        print(f'#{tc} {stack[0]}')
    elif ans==-1 or len(stack)>1:
        print(f'#{tc} error')