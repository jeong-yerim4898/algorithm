a= list(map(int,list(input())))
l = len(a)
dp= [0]*(l+1)
if a[0]==0: #불가능한 경우
    print(0)
else:
    a=[0]+a #인덱스 앞에 하나 추가
    dp[0]=1
    dp[1]=1
    for i in range(2,l+1):
        idx = a[i]
        idx2 = a[i-1]*10+a[i] #전단계 숫자를 합한 경우
        if 0<idx<10:
            dp[i]+=dp[i-1]
        if 9<idx2<27:
            dp[i]+=dp[i-2]
        dp[i]%=1000000

    print(dp[l])