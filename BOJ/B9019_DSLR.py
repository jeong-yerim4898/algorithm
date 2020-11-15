# D (n*2)%10000
# S (n-1) if n>0
# L (n%1000)*10+(n//1000)
# R (n//10)+(n%10)*1000
# BFS 통해 탐색하기
from collections import deque
def bfs(n):
    q=deque([n])
    visited = [0]*10000 # 한번 지나갔던 숫자를 또 bfs 하면 반복이기 때문에 할 필요가 없다.

    while q:
        n =q.popleft()
        if n ==B: # 원하는 결과 값과 같을 경우
            ans = []
            while n !=A: # 결과 값에서 하나씩 되 짚어 보면서 원래 A와 같을 떄를 break point로 생각
                ans.append(path[n][1]) # 해당 위치 DSLR 적기
                n = path[n][0]
            ans.reverse() #뒤에서 부터 넣었기 때문에 뒤짚어 줘야한다.
            print(''.join(ans))
            return
        DSLR_li = [((n*2)%10000),((n-1) if n else 9999),((n%1000)*10+(n//1000)),((n//10)+(n%10)*1000)]
        for i in range(4):
            if not visited[DSLR_li[i]]: #DSLR 연산 후 방문하지 않은 경우
                visited[DSLR_li[i]]=1
                path[DSLR_li[i]]=(n,calculate[i]) # 전 노드의 값을 남기기 추적하기 위해
                q.append(DSLR_li[i])




T =int(input())
for tc in range(T):
    A,B = map(int,input().split())
    calculate = ['D','S','L','R']
    path = [0]*10000 # 해당 숫자의 전단계 남기기
    bfs(A)
