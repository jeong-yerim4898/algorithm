def check_tree(node):
    global cnt
    if node:
        cnt+=1
        check_tree(node_board[node][0])
        check_tree(node_board[node][1])


T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split()) # E간선개수,N 서브트리 루트
    node_info = list(map(int,input().split()))
    node_board = [[0]*2 for _ in range(E+2)]
    for i in range(len(node_info)//2):
        if node_board[node_info[i*2]][0]==0:
            node_board[node_info[i*2]][0]=node_info[i*2+1]
        else:
            node_board[node_info[i * 2]][1] = node_info[i * 2 + 1]
    cnt = 0
    check_tree(N)

    print(f'#{tc} {cnt}')