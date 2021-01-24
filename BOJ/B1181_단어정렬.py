N=int(input())
li=list()
words = set([input() for _ in range(N)])
for n in words:
    word=n
    length = len(word)
    li.append([length,word])
ans_li = sorted(li,key =lambda x:(x[0],x[1]))
for ans in ans_li:
    print(ans[1])