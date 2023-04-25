#0419

#tuple
t1 = (1,2,3,4) # 괄호는 없어도 됨
# 추가 방법
#1
t2 = t1 + (5,6,7,8)
print(t2)
#2
l1 = list(t1)
for i in range(5,9):
    l1.append(i)
t3 = tuple(l1)
print(t3)

#dictionary

student = {}
lect = dict()

#추가방법
student[101] = "홍길동"
student[102] = "김철수"
student[103] = "박정호"
print(student)

lect["강좌명"] = "파이썬"
lect["개설년도"] = 2023
lect["수강생"] = ['홍','김','이','박']
lect["인원"] = 35
print(lect)

lect.update({'인원':10})
lect.update({'강의실':213,'교수':'이희진'})
print(lect)


#
month = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
for i in month:
    print(month[i])
for v in month.values():
    print(v)
for i in month.items():
    print(i[1])

print(month.keys(),'\n',month.values(),'\n',month.items())

# dictionary 삭제
print(month)
print("month.pop(1) : ",month.pop(1))
print(month)
# 마지막으로 삽입된 키의 튜플을 반환하고 키 항목 삭제
print('month.popitem() :', month.popitem())
print(month)