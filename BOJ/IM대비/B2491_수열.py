
N = int(input()) # 수열의 길이
num= list(map(int,input().split()))
plus_cnt = 1
minus_cnt=1
ans = 1
for i in range(N-1):
    if num[i]<num[i+1]:
        plus_cnt+=1
        minus_cnt=1
    elif num[i]>num[i+1]:
        plus_cnt=1
        minus_cnt+=1
    elif num[i]==num[i+1]:
        plus_cnt+=1
        minus_cnt+=1
    if ans<plus_cnt:
        ans= plus_cnt
    elif ans<minus_cnt:
        ans=minus_cnt
print(ans)