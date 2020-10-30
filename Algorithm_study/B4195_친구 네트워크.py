#union-find 부분집합

def find_parent(a): #부모 찾기
    if parent[a]==a:
        return a
    else:
        new_parent = find_parent(parent[a])
        parent[a]=new_parent
        return parent[a]


def union(a,b): #노드 합치기
    a = find_parent(a) # 부모 찾기
    b = find_parent(b) # 부모 찾기
    if a!=b: #만약 a,b의 부모가 다르다면
        parent[b]=a
        cnt[a]+=cnt[b]

T = int(input())
for tc in range(1,T+1):
    parent = dict()
    cnt=dict()
    for _ in range(int(input())):
        f1,f2 = input().split()
        if f1 not in parent:  # 부모가 없는 경우 자기 자선이 부모가 된다.
            parent[f1] = f1
            cnt[f1] = 1
        if f2 not in parent:
            parent[f2] =f2
            cnt[f2] = 1

        union(f1,f2)
        # print(parent)
        # print(cnt)
        print(cnt[find_parent(f1)])
