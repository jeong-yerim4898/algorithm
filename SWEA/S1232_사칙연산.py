# 후위순회 -> 부모 노드에 결과값  넣기
# 완전 이진트리
def in_order(node):
    if node:
        in_order(tree[node][1])
        in_order(tree[node][2])
        result.append(tree[node][0])

for tc in range(1,11):
    N = int(input()) # 노드 개수
    tree = [[0]*3 for _ in range(N+1)]
    result = list()
    for i in range(1,N+1):
        info = input().split()
        tree[i][0] = info[1] if info[1] in ['+','-','*','/'] else int(info[1])
        if len(info)>=3:
            tree[i][1]=int(info[2])
            tree[i][2] = int(info[3])
    # print(tree)
    in_order(1)
    # print(result)
    stack=list()
    while result:
        s= result.pop(0)
        if s not in ['+','-','*','/']:
            stack.append(s)
        else:
            if s == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b)+float(a))
            if s == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b) - float(a))
            if s == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b) / float(a))
            if s == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b) * float(a))
    print(f'#{tc} {int(stack[0])}')