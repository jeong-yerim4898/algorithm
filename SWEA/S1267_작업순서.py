
for tc in range(1,11):
    V,E = map(int,input().split())
    info = list(map(int,input().split()))
    info2 = [info[i:i+2] for i in range(0,E*2,2)]
    board =[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s,e =info2[i]
        board[e][s]=1

    ans=[]
    while True:
        if len(ans)==V:
            break
        start_node = []
        for y in range(1,V+1):
            if 1 not in board[y] and y not in ans:
                start_node.append(y)

        for y in start_node:
            ans.append(y)
            for x in range(V+1):
                board[x][y]=0
    result=" "
    print(f'#{tc}',end="")
    for i in range(len(ans)):
        result += str(ans[i])+" "
    print(result)


