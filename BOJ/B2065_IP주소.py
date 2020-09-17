def network(address):
    network_li = list()
    change = 24
    for i in range(4):
        network_li.append(((address>>change)&(1<<8)-1))
        change-=8
    print("{}.{}.{}.{}".format(network_li[0], network_li[1], network_li[2], network_li[3]))


N = int(input())
ip = [0]*10001
# 32개의 비트로 만들기
for i in range(N):
    a = list(map(int, input().split('.')))
    for j in range(4):
        ip[i]<<=8
        ip[i] |= a[j]
    # print(format(ip[i],'b'))
# print(ip)

# 31개부터 하나씩 비교하고 다른게 나오면 break
mask = 0
for i in range(31,-1,-1):
    bit = 1<<i
    print(format(bit,'b'))
    end= 0
    for j in range(1,N):
        if (ip[0]&bit) != (ip[j]&bit):
            end=1
            break
    if end:
        break
    else:
        mask |= bit


# 임의의 ip주소 & 마스크 = 네트워크 주소
network(ip[0]&mask)
# # 네트트워크 마스크
network(mask)
# print(list(range(31,-1,-1)))