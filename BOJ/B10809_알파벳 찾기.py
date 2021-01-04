S=input()
li=[-1]*26
pos=-1
for s in range(len(S)):
    pos+=1
    if li[ord(S[s])-97]== -1:
        li[ord(S[s])-97]=pos
print(*li)