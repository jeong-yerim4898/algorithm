n,m=map(int,input().split())
if n<101 and n%2 and 0<m<4:
    if m==1:
        tmp=0
        num=0
        for i in range(1,n+1):
            if i%2==0: #짝수인 겨우
                num=num+i
                tmp=num
                for j in range(1,i+1):
                    print(tmp,end=' ')
                    tmp-=1
            else:
                num+=1
                for j in range(1,i+1):
                    print(num,end=' ')
                    num+=1
                num-=1
            print()

    elif m==2:
        num=0
        cnt=2*n-1
        for i in range(1,n+1):
            for j in range(1,2*i-1):
                print(' ',end='')
            for k in range(1,cnt+1):
                print(i-1,end=' ')
            num+=1
            cnt-=2
            print()

    elif m==3:
        end=1
        for i in range(1,n+1):
            num=1
            for j in range(1,end+1):
                print(num,end=' ')
                num+=1
            if i<n//2+1:
                end+=1
            else:
                end-=1
            print()
else:
    print('INPUT ERROR!')