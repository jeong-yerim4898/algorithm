score = input()
idx = len(score)//2
tmp1=0
tmp2=0
for i in score[:idx]:
    tmp1+= int(i)
for i in score[idx:]:
    tmp2+= int(i)
if tmp1==tmp2:
    print('LUCKY')
else:
    print('READY')