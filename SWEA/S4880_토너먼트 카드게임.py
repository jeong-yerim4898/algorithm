def game(x,y):
    if (cards[x-1]==1 and cards[y-1]==3) or (cards[x-1]==1 and cards[y-1]==1):
        return x
    elif (cards[x-1]==2 and cards[y-1]==1) or (cards[x-1]==2 and cards[y-1]==2):
        return x
    elif (cards[x-1]==3 and cards[y-1]==2) or (cards[x-1]==3 and cards[y-1]==3):
        return x
    return y


def grouping(start,end):
    if start==end:
        return start

    left = grouping(start,(start+end)//2)
    right = grouping((start+end)//2+1,end)
    return game(left,right)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))
    start = 1
    end = N

    print(f'#{tc} {grouping(start,end)}')