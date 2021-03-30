def dfs(n,depth):
    global min_val,cnt
    if n==B:
        print(depth)
        exit(0)
        return
    if n<B:
        dfs(n*2,depth+1)
        dfs(int(str(n)+'1'),depth+1)



A,B = map(int,input().split())
min_val = 987654321
cnt=0
dfs(A,1)
print(-1)