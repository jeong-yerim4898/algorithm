board=[['']*15 for _ in range(5)]
for i in range(5):
    s = list(input())
    for j in range(len(s)):
        board[i][j]=s[j]
ans=''
for c in range(15):
    for r in range(5):
        ans+=board[r][c]
print(ans)