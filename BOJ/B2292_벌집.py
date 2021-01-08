N = int(input())
start =1
multi=6
cnt=1
if N==1:
    print(1)
else:
    while True:
        start += multi
        cnt+=1
        if N<=start:
            print(cnt)
            break
        multi+=6
