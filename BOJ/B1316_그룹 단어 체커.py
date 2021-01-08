T = int(input())
cnt=0
for tc in range(1,T+1):
    sen = input()
    for j in range(len(sen)-1):
        if sen[j]==sen[j+1]:
            pass
        elif sen[j] in sen[j+1:]:
            break
    else:
        cnt+=1
print(cnt)



