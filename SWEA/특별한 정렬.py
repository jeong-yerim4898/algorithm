def orum(li):
    N = len(li)
    for i in range(N):
        minidx = i
        for j in range(i+1,N):
            if li[minidx]<li[j]:
                minidx = j
        li[i],li[minidx] = li[minidx],li[i]
    return li

T = int(input())
for test_case in range(1,T+1):
    turn = int(input())
    nums = list(map(int,input().split()))
    N = len(nums)
    sort_list = orum(nums)
    #정렬
    result=[0]*N
    for k in range(0,N//2):
        result[k*2] = sort_list[k]
    for j in range(1,(N//2)+1):
        result[(j*2)-1] = sort_list[N-j]

    print(f'#{test_case}',end=' ')
    for i in range(10):
        print(result[i],end=' ')
    print()