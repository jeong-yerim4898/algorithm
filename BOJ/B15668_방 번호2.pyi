N = int(input())
for a in range(1,min(100000, N)):
    b=N-a
    if b>=1:
        new_str= str(a)+str(b)
        if len(new_str)==len(set(new_str)):
            print(str(a)+' + '+str(b))
            break
else:
    print(-1)
