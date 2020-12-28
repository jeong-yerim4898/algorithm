s = list(input())
koi=0
ioi=0
for i in range(len(s)):
    if s[i:i+3] == ['K','O','I']:
        koi+=1
    if s[i:i+3] == ['I','O','I']:
        ioi+=1
print(koi)
print(ioi)