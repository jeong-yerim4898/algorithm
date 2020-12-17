num1=int(input())
num2=int(input())
num3=int(input())
tmp = str(num1*num2*num3)
li =[0]*10
for i in tmp:
    li[int(i)]+=1
for k in li:
    print(k)