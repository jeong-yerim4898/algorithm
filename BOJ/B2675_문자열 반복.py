T=int(input())
for tc in range(1,T+1):
    N,S = map(str,input().split())
    for s in S:
        print(s*int(N),end='')
    print()