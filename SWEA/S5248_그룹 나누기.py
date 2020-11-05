def find_set(n):
    if n == parent[n]:
        return n
    else:
        return find_set(parent[n])

def union(a,b):
    b_parent = find_set(b)
    parent[b_parent]  = find_set(a)


T= int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    parent = [0]*(N+1)

    for i in range(1,N+1):
        parent[i]=i # 모두가 첨에는 자기 자신이 부모

    data = list(map(int,input().split()))
    for i in range(M): #관계수 반복
        s = data[i*2]
        e = data[i*2+1]
        union(s,e) # 자식과 부모
    result = list()
    for i in range(len(parent)):
        result.append(find_set(i))

    print(f'#{tc} {len(set(result))-1}')