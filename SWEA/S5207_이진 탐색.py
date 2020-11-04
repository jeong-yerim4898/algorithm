def binary_search(L,low,high,key,dir): # 길이,리스트.원하는 숫자
    global cnt,check
    if low>high:
        return
    else:
        middle = (low+high)//2
        if key == L[middle]:
            check = 1
            return
        elif key<L[middle]:
            if dir=='L':
                return
            else:
                return binary_search(L,low,middle-1,key,'L')
        else:
            if dir=='R':
                return
            else:
             return binary_search(L,middle+1,high,key,'R')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #A갯수 B갯수
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    cnt = 0
    for b in B:
        check = 0
        if b in A:
            binary_search(A,0,len(A)-1,b,0)
            if check ==1:
                cnt+=1
    print(f'#{tc} {cnt}')