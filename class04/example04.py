#메소드
str_a = "하하하"
str_b = str_a.replace('하','호')
print(str_a)
print(str_b)

str_c = "안녕하세요. " + "파이썬." * 10
print(str_c.replace("파이썬", "자바", 5))

#6자리 실수를 입력받는다. ex) 222.788
#출력 : 실수의 각 자리의 합을 출력. ex) 2+2+2+7+8+8
question = input("6자리 실수를 입력하시오")
question = question.replace(".","")
sum = 0
for i in question:
    sum += int(i)
print("모든 자리수의 합은 : " , sum)
