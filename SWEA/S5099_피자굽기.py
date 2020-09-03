def bfs():
    global result
    q = list()
    for i in range(N):
        q.append([pizza[i],i])

    k = 0
    while len(q)!=1:
        q[0][0]//=2
        # 1번자리 체크

        if q[0][0]==0: # 치즈 다녹음
            if N+k<M: # 피자 갯수보다 적으면
                q.pop(0)
                q.append([pizza[N+k],N+k])
                k+=1
            elif N+k>=M: # 피자 갯수보다 같거나 많으면
                q.pop(0)
        else: # 치즈 덜녹음 (원형 큐)
            q.append(q.pop(0))
    result = q[0][1]
    return



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    result = 0
    bfs()
    print(f'#{tc} {result+1}')