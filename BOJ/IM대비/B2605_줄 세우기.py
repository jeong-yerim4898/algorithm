
N = int(input())
lucky = list(map(int,input().split()))

li=list()
c = 0
for i in lucky:
    li.insert(c-i,c+1)
    c+=1
for i in li:
    print(i,end=' ')
