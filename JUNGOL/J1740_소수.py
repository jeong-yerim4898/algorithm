def isprime(n):
    if n<2:
        return False
    k=2
    for k in range(2,(n//k)+1):
        if n%k==0:
            return 0
    return 1

M= int(input())
N = int(input())
nums = list()
for n in range(M,N+1):
    if n<2:
        pass
    elif isprime(n):
        nums.append(n)
if len(nums)==0:
    print(-1)
else:
    print(sum(nums))
    print(nums[0])