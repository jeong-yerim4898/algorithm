N,M = map(int,input().split())
time_cases ={
    'none':0,
    '3multi':((N-1)//3)+1,
    'even': (N//2),
    'odd': (N//2) if N%2==0 else N//2+1,
    'even+3multi':(N//2)+((N-1)//3)+1,
    'odd+3multi':((N//2) if N%2==0 else N//2+1)+((N-1)//3)+1,
    'all':N,
    'all+3multi':N+(((N-1)//3)+1),
}
max_case=0
if N==1:
    if M==0:
        print(1)
    else:
        print(2)
elif N==2:
    if M==0:
        print(1)
    elif M==1:
        print(3)
    else:
        print(4)
else:
    for v in time_cases.values():
        if v>M:
            break
        else:
            max_case+=1
    print(max_case)