
C = int(input())
student = list(map(int,input().split()))
con = list(map(int,input().split()))
ans = 0

for k in range(C):
    if student[k]!=0:
        ans+=1
        student[k]-=con[0]
for m in range(C):
    if student[m]<=0:
        continue
    elif student[m]%con[1]==0:
        ans+= student[m]//con[1]
    else:
        ans+= student[m]//con[1]+1
print(ans)