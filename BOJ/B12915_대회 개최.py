arr = list(map(int,input().split(' ')))
cnt=0
while True:
    if arr[0]>0:
        arr[0]-=1
    else:
        if arr[1]>0:
            arr[1]-=1
        else:
            break

    if arr[2]>0:
        arr[2]-=1
    else:
        if arr[1]>0 or arr[3]>0:
            if arr[1]>=arr[3]:
                arr[1]-=1
            elif arr[1]<arr[3]:
                arr[3]-=1
            else:
                break

    if arr[4]>0:
        arr[4]-=1
    else:
        if arr[3]>0:
            arr[3]-=1
        else:
            break
    cnt+=1
print(cnt)

