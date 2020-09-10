
T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split()) # 노드개수, 리프노드 개수, 출력할 노드 번호
    node_info = [0]*(N+1)
    sum_node = [0]*(N+1)
    for i in range(M):
        idx,val = map(int,input().split())
        node_info[idx] = val
    # print(node_info)

    for j in range(N,0,-1):
        n = j//2
        node_info[n]+=node_info[j]
    print(f'#{tc} {node_info[L]}')