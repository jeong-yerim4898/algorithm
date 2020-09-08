def powerset(worker,idx):
    global min_h
    if idx==N:
        sum_h=0
        for i in range(N):
            if worker[i]!=0:
                sum_h+=height[i]
        if sum_h>=B and (sum_h-B)<min_h:
            min_h = sum_h-B
        return

    worker[idx]=1
    powerset(worker,idx+1)
    worker[idx]=0
    powerset(worker,idx+1)


T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    height = list(map(int,input().split()))
    min_h =987654321
    worker = [0]*N
    powerset(worker,0)
    print(f'#{tc} {min_h}')