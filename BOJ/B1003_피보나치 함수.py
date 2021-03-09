T= int(input())
fibo =[[0,0] for _ in range(41)]
fibo[0]=[1,0]
fibo[1] = [0,1]
# print(fibo)
for tc in range(T):
    n = int(input())
    for i in range(2,41):
        fibo[i][0] = fibo[i-1][0]+fibo[i-2][0]
        fibo[i][1] = fibo[i-1][1]+fibo[i-2][1]
    print(str(fibo[n][0])+' '+str(fibo[n][1]))

