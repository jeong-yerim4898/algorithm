alpabet = 'abcdefghijknmlopqrstuvwxyz'
dic = dict()
enc = list(input())
sentence = list(input())
for e in range(len(enc)):
    dic[alpabet[e]]=enc[e]
for s in sentence:
    if s ==' ':
        print(' ',end='')
    elif 64<ord(s)<96:
        print(dic[s.lower()].upper(),end='')
    else:
        print(dic[s],end='')