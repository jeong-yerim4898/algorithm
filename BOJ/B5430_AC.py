#reverse를 사용하면 무조거 터진다.
T = int(input())
for tc in range(1,T+1):
    fun = input().replace('RR','')
    fun = list(fun)
    n = int(input())
    li = input()[1:-1].split(',')
    ans=0
    for k in range(len(fun)):
        if n==0:
            ans='error'
            break
        if fun[k]=='R':
            li.reverse()
        else:
            if len(li)==0:
                ans='error'
                break
            else:
                li=li[1:]
    if ans=='error':
        print(ans)
    else:
        print('[',end='')
        for i in li[:-1]:
            print(int(i),end=',')
        print(li[-1],end=']')
        print()