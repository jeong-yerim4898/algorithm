

def dfs(cnt):
    global result
    if cnt == 15:
        if w.count(0)==6 and s.count(0)==6 and l.count(0)==6:
            result = 1
        return
    id1,id2 = case[cnt][0],case[cnt][1]
    if w[id1]>0 and l[id2]>0:
        w[id1]-=1
        l[id2]-=1
        dfs(cnt+1)
        w[id1]+=1
        l[id2]+=1
    if w[id2]>0 and l[id1]>0:
        w[id2]-=1
        l[id1]-=1
        dfs(cnt+1)
        w[id2]+=1
        l[id1]+=1

    if s[id1]>0 and s[id2]>=0:
        s[id1]-=1
        s[id2]-=1
        dfs(cnt+1)
        s[id1]+=1
        s[id2]+=1
# 이길때 질때 무승부
case = list()
for i in range(6):
    for j in range(i+1,i+6):
        case.append((i,j))
# A:0 B:1 C:2 D:3 E:4 F:5
for i in range(4):
    result = 0
    data = list(map(int,input().split()))
    w =list()
    s = list()
    l = list(())
    for j in range(0,18,3):
        w.append(data[j])
        s.append(data[j+1])
        l.append(data[j+2])
    dfs(0)
    print(w)
    print(s)
    print(l)
    print(result)
