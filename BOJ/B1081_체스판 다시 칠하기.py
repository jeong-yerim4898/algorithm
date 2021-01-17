M,N = map(int,input().split())
mapping = [list(input()) for _ in range(M)]
ans=list()
for r in range(M-7):
    for c in range(N-7):
        start=mapping[r][c]
        cnt1=0
        cnt2=0
        for i in range(r,r+8):
            for j in range(c,c+8):
                if (i+j)%2==0:
                    if mapping[i][j]!='B':
                        cnt1+=1
                    if mapping[i][j]!='W':
                        cnt2+=1
                else:
                    if mapping[i][j] !='W':
                        cnt1+=1
                    if mapping[i][j] !='B':
                        cnt2+=1
        ans.append(cnt1)
        ans.append(cnt2)
print(min(ans))