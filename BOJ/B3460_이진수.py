T = int(input())
for tc in range(1,T+1):
    n = int(input())
    bi = bin(n)
    bi_str = bi[2:]
    for i in range(len(bi_str)-1,-1,-1):
        if bi_str[i]=='1':
            print(len(bi_str)-1-i,end=' ')
#B10818 최소최대
N=int(input())
li=list(map(int,input().split()))
print(str(min(li))+' '+str(max(li)))