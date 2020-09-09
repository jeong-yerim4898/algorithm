def in_order(node):
    if node!='0':
        in_order(bi_tree[node][1])
        print(bi_tree[node][0],end="")
        in_order(bi_tree[node][2])

for tc in range(1,11):
    N = int(input())
    bi_tree = {}
    for i in range(N):
        node_info = input().split()
        if len(node_info)!=4:
            for _ in range(4-len(node_info)):
                node_info.append('0')
        bi_tree[node_info[0]]=node_info[1:4]
    print(f'#{tc}',end=" ")
    in_order('1')
    print()