sen = input()
sign = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ans=0
idx=0
while idx<len(sen):
    if sen[idx:idx+2] in sign:
        ans+=1
        idx+=2
    elif sen[idx:idx+3]=='dz=':
        ans+=1
        idx+=3
    else:
        idx+=1
        ans+=1
print(ans)