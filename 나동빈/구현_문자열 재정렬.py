'''
K1KA5CB7
AJKDLSI412K4JSJ9D
'''
a = input()
a_li = sorted(a)
alp = [a for a in a_li if a not in ['0','1','2','3','4','5','6','7','8','9']]
num = [int(a) for a in a_li if a in ['0','1','2','3','4','5','6','7','8','9']]
for i in alp:
    print(i,end='')
print(sum(num))