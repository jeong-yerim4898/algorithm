from collections import defaultdict

N,M = map(int,input().split()) # 재료개수, 공식개수
material = defaultdict(list)
for _ in range(N):
    m,c = map(str,input().split())
    material[m]=int(c)
for _ in range(M):
    pass