import re
def solution(files):
    # 문자와 숫자 기준으로 분리하기
    file_seperate=[re.split(r'([0-9]+)',file) for file in files]
    # 문자먼저 배열하고 숫자 정렬하기
    file_sort = sorted(file_seperate,key=lambda x: (x[0].lower(),int(x[1])))

    # 정렬한 리스트 합치기

    return ["".join(file) for file in file_sort]