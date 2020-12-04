def game(input_li):
    li = []
    tmp = 0

    for num in input_li:
        if num: #0이라면 버림
            if not tmp:
                tmp=num
            else:
                if tmp==num:
                    li.append(tmp*2)
                    tmp=0
                else:
                    li.append(tmp)
                    tmp=num
    if tmp:
        li.append(tmp)
    for _ in range(len(input_li)-len(li)):
        li.append(0)
    return li

T= int(input())
for tc in range(1,T+1):
    N,S = map(str,input().split())
    N = int(N)
    mapping = [list(map(int,input().split())) for _ in range(N)]
    if S=='up':
        for c in range(N):
            tmp_up=list()
            for r in range(N):
                tmp_up.append(mapping[r][c])
            tmp_up=game(tmp_up)
            for r in range(N):
                mapping[r][c]=tmp_up[r]

    elif S=='down':
        for c in range(N):
            tmp_down=list()
            for r in range(N):
                tmp_down.append(mapping[-1-r][c])
            tmp_down=game(tmp_down)
            for r in range(N):
                mapping[-1-r][c]=tmp_down[r]
    elif S=='right':
        for r in range(N):
            mapping[r]=game(mapping[r][::-1])[::-1]
    else:
        for r in range(N):
            mapping[r]=game(mapping[r])
    print(f'#{tc}')
    for r in range(N):
        print(*mapping[r])
