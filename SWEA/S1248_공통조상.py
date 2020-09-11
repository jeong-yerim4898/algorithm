def check_tree(node):
    global cnt
    if node:
        cnt+=1
        check_tree(tree[node][0])
        check_tree(tree[node][1])
    return cnt

def find_par(node):
    par=[]
    while node>1:
        node = tree[node][2]
        par.append(node)
    return par

T = int(input())
for tc in range(1,T+1):
    V,E,a,b = map(int,input().split())
    node_info= list(map(int,input().split()))
    tree=[[0]*3 for _ in range(V+1)]
    for i in range(E):
        if tree[node_info[i*2]][0]:
            tree[node_info[i*2]][1]= node_info[i*2+1]
        else:
            tree[node_info[i*2]][0]= node_info[i*2+1]
        tree[node_info[i*2+1]][2]=node_info[i*2]
    a_par = find_par(a)
    b_par = find_par(b)
    cnt= 0
    # print(tree)
    # same_par = list(set(a_par)&set(b_par))
    for par in a_par:
        if par in b_par:
            ans= par
            break
    # par= max(same_par)
    print(f'#{tc} {ans} {check_tree(ans)}')
