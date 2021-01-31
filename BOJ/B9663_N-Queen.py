# row는 신경 쓰지 않는다 무조건 1행 1퀸이기 때문
N=int(input())
ans=0
a,b,c=[False]*N,[False]*(2*N-1),[False]*(2*N-1)

def solve(i):
    global ans
    if i==N:
        ans+=1
        return
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j]=b[i+j]=c[i-j+N-1]=True
            solve(i+1)
            a[j] = b[i + j] = c[i - j + N - 1] = False
solve(0)
print(ans)