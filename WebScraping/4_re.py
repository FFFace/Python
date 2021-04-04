import re

# . -> 문자 하나            ex) ca.e    | care, cafe, case
# ^ -> 문자열 시작          ex) ^de     | desk, destination 
# $ -> 문자열 끝            ex) e$      | case, base

def print_match(m):
    if m:
        print("m.group() : ",m.group())        # 일치하는 문자열 반환
        print("m.string : ", m.string)          # 입력받은 문자열
        print("m.start() : ", m.start())        # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())            # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())          # 일치하는 문자열의 (시작, 끝) index 
    else:
        print("Error!")

p = re.compile("ca.e")              # re.compile(str) : 규칙 정의

m = p.match("care")                 # match(str) : 문자열이 규칙과 일치하면 str 반환
print_match(m)

m = p.search("good care")           # search(str) : 문자열 중 규칙과 일치하는 항목이 있으면 str 반환
print_match(m)

lst = p.findall("good care cafe")   # findall(str) : 문자열 중 규칙과 일치하는 모든 항목 반환
print(lst)
