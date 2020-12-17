n = int(input())
nums = list(map(int,input().split()))
m = int(input())
drug=[0]*(m+1)
ans=0
ans2=0
for i in range(1,m+1):
    if m%i==0:
        drug[i]=1
for k in nums:
    if k<m+1:
        if drug[k]==1:
            ans+=k
    if k%m==0:
        ans2+=k
print(ans)
print(ans2)
