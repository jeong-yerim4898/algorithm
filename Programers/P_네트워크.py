n=int(input())
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
answer = 0
nodes = [0]*n
q=list()
q.append(0)
nodes[0]=1
while q:
    s_node = q.pop(0)
    nodes[s_node]=1
    for n_node in range(n):
        if computers[s_node][n_node] and not nodes[n_node]:
            nodes[n_node]=1
            q.append(n_node)
            answer+=1
print(answer)