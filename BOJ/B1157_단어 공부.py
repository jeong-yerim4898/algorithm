from collections import defaultdict
S=input().lower()
li_dict = defaultdict(int)
for s in S:
    li_dict[s]+=1
maxxim = max(li_dict.items(),key=lambda x:x[1])
cnt = [n[1] for n in li_dict.items()].count(maxxim[1])
if cnt>1:
    print('?')
else:
    print(maxxim[0].upper())