from itertools import combinations
def is_prime(N):
    if N<2:
        return False
    else:
        for i in range(2,int(N**0.5)+1):
            if N%i==0:
                return False
        else:
            return True

num_li=[]
N= int(input())
for n in range(2,N+1):
    if is_prime(n)==True:
        num_li.append(n)
print(num_li)
if not num_li:
    print(-1)
    exit(0)
for i in range(2,len(num_li)):
   for a in list(combinations(num_li,i)):
       ans=1
       for ele in a:
           ans*=ele
       if ans==N:
           print(*a)
           exit(0)