from math import sqrt
n= int(input())
nums = [0]*10000
cnt=0
sq = int(sqrt(n))
for i in range(1,sq+1):
    if n%i==0:
        nums[cnt]=i
        cnt+=1
        if n//i !=i:
            nums[cnt]=n//i
            cnt+=1
num2=nums[:cnt]
num2.sort()
for i in num2:
    print(i,end=' ')