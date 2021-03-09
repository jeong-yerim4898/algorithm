def calcul(idx,val,add,sub,multi,division):
    global min_val,max_val
    if idx==N: # 마지막 idx면
        if val<min_val:
            min_val=val
        if val>max_val:
            max_val=val
    if add:
        calcul(idx+1,val+A[idx],add-1,sub,multi,division)
    if sub:
        calcul(idx+1,val-A[idx],add,sub-1,multi,division)
    if multi:
        calcul(idx+1,val*A[idx],add,sub,multi-1,division)
    if division:
        calcul(idx+1,val//A[idx] if val>=0 else -1*((val*-1)//A[idx]),add,sub,multi,division-1)

N = int(input())
A = list(map(int,input().split()))
op = list(map(int,input().split()))
min_val = 9999999999
max_val = -99999999999999
calcul(1,A[0],op[0],op[1],op[2],op[3])
print(max_val)
print(min_val)