N = int(input())
li_person=list()
for _ in range(N):
    weight,height = map(int,input().split())
    li_person.append((weight,height))
for person in li_person:
    cnt=1
    for idx in range(N):
        if person[0]<li_person[idx][0]:
            if person[1]<li_person[idx][1]:
                cnt+=1
    print(cnt,end=' ')