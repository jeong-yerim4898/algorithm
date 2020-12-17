# a=int(input())
# b=list(map(int,list(input())))
# k = 1
# ans=0
# for i in range(2,-1,-1):
#     ans += (a*b[i])*k
#     print(a*b[i])
#     k*=10
# print(ans)

num1 = int(input())
num2 = int(input())
print(num1*(num2%10))
print(num1*((num2%100)//10))
print(num1*(num2//100))
print(num1*num2)
