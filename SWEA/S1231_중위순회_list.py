def in_order(node):
    if node:
        in_order(bi_tree[node][1])
        print(bi_tree[node][0],end="")
        in_order(bi_tree[node][2])

for tc in range(1,11):
    N = int(input())
    bi_tree = [[0]*3 for _ in range(N+1)]
    for k in range(N):
        tree_info = input().split()
        idx = int(tree_info[0])
        bi_tree[idx][0]=tree_info[1]
        if len(tree_info)>2:
            for j in range(len(tree_info)-2):
                bi_tree[idx][j+1]=int(tree_info[j+2])
    # print(bi_tree) 트리 2중 행렬확인
    print(f'#{tc}',end=" ")
    in_order(1)
    print()