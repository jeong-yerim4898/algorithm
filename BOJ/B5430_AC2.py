T = int(input())
for tc in range(1,T+1):
    fun = input().replace('RR','')
    fun = list(fun)
    n = int(input())
    li = input()[1:-1].split(',')
    ans=0
    l,r,d = 0,0,True
    for c in fun:
        if c=='R':
            d = not d
        elif c=='D':
            if d:
                l+=1
            else:
                r+=1
    if l+r<=n:
        res=li[l:n-r]
        if d:
            print('['+','.join(res)+']')
        else:
            print('['+','.join(res[::-1])+']')
    else:
        print('error')