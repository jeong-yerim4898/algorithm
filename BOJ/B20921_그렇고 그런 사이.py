visited = [0]*5005
ans = [-1]*5005
N,K = map(int,input().split())
s=1
e = N
idx=1
while K:
    if K>=e-1:
        K-=e-1
        ans[idx]=e
        idx+=1
        visited[e]=True
    e-=1

n=1
for i in range(1,N+1):
    if ans[i]!=-1: # ans에 값이 할당 되었다면
        continue
    while visited[n]: # 이미 사용한 숫자 였다면
        n+=1
    ans[i]=n # ans에 숫자를 할당하고 1 더해준다.
    n+=1
for i in range(1,len(ans)):
    if i==N+1:
        break
    print(ans[i],end=' ')

