def answer0(s):
    return s==s[::-1]

T=int(input())
for test_case in range(1,T+1):
    sen=input()
    if answer0(sen):
        print(0)
        continue
    else:
        #왼쪽고정, 오른쪽 고정
        left,right = True,True
        l,r=0,len(sen)-1
        pal=True
        while l<=r:
            if sen[l]!=sen[r]:
                if pal:
                    pal=False
                    r-=1
                else:
                    left=False
                    break
            else:
                l+=1
                r-=1
        #오른쪽 고정
        l,r=0,len(sen)-1
        pal=True
        while l <= r:
            if sen[l] != sen[r]:
                if pal:
                    pal = False
                    l += 1
                else:
                    right = False
                    break
            else:
                l += 1
                r -= 1
    if not (left or right):
        print(2)
    else:
        print(1)




