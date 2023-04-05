#0405
str = "파이썬수업,파이썬수업,파이썬수업,C수업,파이썬수업,JAVA수업,파이썬수업,파이썬수업" 

#replace
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))

#find, index
print("find : ", str.find("C"), "index : ", str.index("C"))
print(str.find("AI"))    # 없다면 -1 리턴
# print(str.index("AI")) # 없으면 오류

#split
print(str.split(","))

#join 문자열 사이사이 삽입
print("**".join(str))

#format
print(3,'+',4,'=',7)
fo = "{0:d} + {1} = {2}".format(3,4,7)
print(fo)

#boolean
print(type(True),type(False))
a = 'hello'
print(bool(a),bool(-3),)
print(bool(0),bool(""))
print(int(True))