A,B,C = map(int,input().split())
income=C
fix_cost=A+B
n=1
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)