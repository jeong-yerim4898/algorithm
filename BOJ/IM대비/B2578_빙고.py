def check(cnt):
    result = 0
    result += bingo.count([0,0,0,0,0]) #행 갯수확인
    if result >=3:
        print(cnt)
        return True
    for i in range(5): #열 체크
        for j in range(5):
            if bingo[j][i] !=0:
                break
        else:
            result+=1
            if result>=3:
                print(cnt)
                return True
    # 대각선 확인
    if bingo[0][0]==0 and bingo[1][1]==0 and bingo[2][2]==0 and bingo[3][3]==0 and bingo[4][4]==0:
        result +=1
        if result>=3:
            print(cnt)
            return True
    if bingo[0][4]==0 and bingo[1][3]==0 and bingo[2][2]==0 and bingo[3][1]==0 and bingo[4][0]==0:
        result +=1
        if result>=3:
            print(cnt)
            return True
    return False

bingo= [input().split() for _ in range(5)]
cnt = 0

for i in range(5):
    for info in input().split():
        cnt+=1
        state=False
        for j in range(5):
            for k in range(5):
                if info == bingo[j][k]:
                    state= True
                    bingo[j][k]=0
                    c= check(cnt)
                    break
            if state:
                break
        if c:
            break
    if c:
        break
