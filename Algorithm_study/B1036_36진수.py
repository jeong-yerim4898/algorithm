base = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'A':0,'B':0,'C':0,'D':0,
        'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,
        'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'X':0,'Y':0,'Z':0}

N = int(input())
boards = [list(input()) for _ in range(N)]
K = int(input())
for board in boards:
    for ele in board:
        value = base[ele]
        value+=1
        base[ele]=value
print(base)
res= sorted(base.items(),key=(lambda x:x[1]),reverse=True)
change_li =list()
for i in range(K):
    change_li.append(res[i][0])
print(change_li)
for board in boards:
    for j in range(len(board)):
        if board[j] in change_li:
            board[j]='Z'
print(boards)
