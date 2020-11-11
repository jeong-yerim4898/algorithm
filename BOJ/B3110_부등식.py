
B,C,D = map(int,input().split())
A1,A2 = map(int,input().split())
E1,E2 = map(int,input().split())

ans = 0
for c1 in range(int(A1/A2*C)-1,int(C*E1/E2)+1):
    if A1/A2 < c1/C < E1/E2:
        ans += ((B*c1-1)//C -(B*A1//A2)) * ((D*E1-1)//E2-(D*c1//C))
print(ans)