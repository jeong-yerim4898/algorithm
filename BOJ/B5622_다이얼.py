from collections import defaultdict
alpabet =['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
call_num = input()
tmp=0
for num in call_num:
    for al in alpabet:
        if num in al:
            tmp+=alpabet.index(al)+3
print(tmp)

