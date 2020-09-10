# 최소 힙
def heappush(val):
    global heapcnt
    heapcnt+=1
    heap[heapcnt]=val
    cur = heapcnt
    parent = cur//2

    while parent and heap[parent]>heap[cur]:
        heap[parent],heap[cur] = heap[cur],heap[parent]
        cur = parent
        parent = cur//2


T = int(input())
for tc in range(1,T+1):
    N =  int(input())
    num = list(map(int,input().split()))
    heap=[0]*(N+1)
    heapcnt=0
    for i in range(N):
        heappush(num[i]) # 최소 힙 만들기


    sum_par = 0 # 주어진 노드의 조상노드의 값들의 합
    while N>1:
        N //= 2
        sum_par += heap[N]

    print(f'#{tc} {sum_par}')