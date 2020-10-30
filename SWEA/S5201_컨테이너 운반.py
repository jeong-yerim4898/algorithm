
T = int(input())
for tc in range(1,T+1):
    containers , trucks = map(int,input().split())
    con_weight = list(map(int,input().split()))
    con_weight.sort(reverse=True)
    truck_weight = list(map(int,input().split()))
    truck_weight.sort(reverse=True)
    # print(con_weight)
    # print(truck_weight)
    result = 0
    idx = 0
    for cw in con_weight:
        for tw in range(idx,len(truck_weight)):
            if cw<=truck_weight[tw]:
                result+=cw
                idx+=1
                break
    print(f'{tc} {result}')