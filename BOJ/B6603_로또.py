def back(idx,cnt):
    if cnt==6:
        for j in range(6):
            print(lotto[j],end=' ')
        print()
        return
    for i in range(idx,len(S)):
        lotto[cnt]=S[i]
        back(i+1,cnt+1)



lotto = [0 for _ in range(13)]
while True:
    li = list(map(int,input().split()))
    K = li[0]
    S = li[1:]
    if K==0:
        break
    back(0,0)
    print()

