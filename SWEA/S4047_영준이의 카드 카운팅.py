def counting():
    if len(set(cards))!= len(cards):
        return False
    else:
        for j in range(len(cards)):
            if cards[j][0]=='S':
                Svisit[int(cards[j][1:3])]=1
            elif cards[j][0]=='D':
                Dvisit[int(cards[j][1:3])]=1
            elif cards[j][0]=='H':
                Hvisit[int(cards[j][1:3])]=1
            elif cards[j][0]=='C':
                Cvisit[int(cards[j][1:3])]=1

T = int(input())
for tc in range(1,T+1):
    S  = input()
    cards = [S[i:i+3] for i in range(0,len(S),3)]
    Svisit=[0]*14
    Dvisit = [0] * 14
    Hvisit = [0] * 14
    Cvisit = [0] * 14

    if counting()==False:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {Svisit.count(0)-1} {Dvisit.count(0)-1} {Hvisit.count(0)-1} {Cvisit.count(0)-1}')
