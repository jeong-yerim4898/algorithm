from collections import deque

N ,K = map(int,input().split())
numbers = list(input().split())

#bfs
visit = set("".join(numbers))
queue=deque([["".join(numbers),0]])

ans=-1
while queue:
    candidate,cnt = queue.popleft()
    newsort = list(candidate)

    if newsort == sorted(newsort):
        ans=cnt
        break

    for i in range(N-K+1):
        new_li = list(newsort)
        target = new_li[i:i+K]
        target.reverse()
        for j in range(K):
            new_li[i+j] = target[j]
        newcadidate = "".join(new_li)
        if newcadidate not in visit:
            visit.add(newcadidate)
            queue.append([newcadidate,cnt+1])
print(ans)

