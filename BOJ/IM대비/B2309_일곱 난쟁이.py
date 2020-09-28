
h_li = list()
for _ in range(9):
    h_li.append(int(input()))

h_li.sort()
ans = sum(h_li)
for i in range(9):
    for j in range(i+1,9):
        if ans-h_li[i]-h_li[j]==100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(h_li[k])
            exit()