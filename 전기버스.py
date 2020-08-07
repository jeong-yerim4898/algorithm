T = int(input())
for test_case in range(1,T+1):
    bus_state = 0
    charge_cnt = 0
    max_move, station, charge_n = map(int,input().split())
    charge_li = list(map(int,input().split(' ')))

    move = max_move
    while bus_state<station:
        if (bus_state+move) == station:
            break
        elif (bus_state+move) in charge_li:
            charge_cnt+=1
            bus_state += move
            move = max_move
        else:
            move-=1
            if move == 0:
                charge_cnt = 0
                break
    print(f'#{test_case} {charge_cnt}')


