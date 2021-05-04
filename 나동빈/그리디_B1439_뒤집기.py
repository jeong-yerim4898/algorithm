S = input()
zero_cnt =0 # 1 to 0
one_cnt=0 # 0 to 1
for i in range(1,len(S)):
    if S[i-1]!=S[i]: # 전과 다음 문자열이 다르다면?
        if S[i-1]=='0':
            one_cnt+=1
        else:
            zero_cnt+=1

if S[-1]=='0':
    one_cnt+=1
else:
    zero_cnt+=1
print(min(zero_cnt,one_cnt))
