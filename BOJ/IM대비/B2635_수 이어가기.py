N = int(input())
max_cnt=0
max_li = list()

for i in range(1,N+1):
    tmp=[N,i]
    while True:
        res = tmp[-2]-tmp[-1]
        if res<0:
            if len(tmp)>max_cnt:
                max_cnt= len(tmp)
                max_li=tmp
            break
        else:
            tmp.append(res)

print(max_cnt)
print(*max_li)