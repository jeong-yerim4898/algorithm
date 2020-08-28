import sys
sys.setrecursionlimit(100000)

def hotel(customer,city):
    minimum = 100*10000
    cost = 0
    if customer <=0:
        return 0
    elif total[customer]>0:
        return total[customer]

    else:
        for i in range(city):
            cost = hotel(customer-ad[i][1],city)+ad[i][0]
            minimum = cost if cost<minimum else minimum
        total[customer] = minimum
        return minimum

customer, city = map(int,input().split())
ad =[list(map(int,input().split())) for _ in range(city)]
total = [0]*9999


print(hotel(customer,city))