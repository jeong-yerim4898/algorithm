def in_order(node):
    global val
    if node<=N:
        in_order(node*2) # 왼쪽
        tree[node]=val
        val+=1
        in_order(node*2+1) # 오른쪽



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)
    val = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')