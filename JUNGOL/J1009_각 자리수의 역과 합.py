flag = True

while flag:
    num = int(input())
    if num==0:
        break
    else:
        sum=0
        a=0
        b=0
        while num:
            a=(a*10)+(num%10)
            sum+=num%10
            num//=10
        print(a,sum)