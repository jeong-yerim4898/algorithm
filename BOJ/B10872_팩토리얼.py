def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n*factorial(n-1)

N = int(input())
if N==0:
    print(1)
else:
    print(factorial(N))