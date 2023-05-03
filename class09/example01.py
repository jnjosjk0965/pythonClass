#0503
#함수
#name - add3 function - 3 더함 input - 숫자 1개 output - 연산결과인 숫자 1개
def add3(num):
    return num + 3

result = add3(5)
print(result)

def printName(name1,name2):
    print("안녕",name1,',안녕',name2)
    return None

printName("윈터","카리나")

def addNum(num1,num2):
    return num1+num2

print(addNum(4,6))

'''
mySum 인자는 몇개가 들어올지 모름
결과 - 모든 인자의 합을 return
'''
def mySum(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
print(mySum(4,2,3,23,12,31,23,32,2312,3,123,12,321,3,123,1232,21,3,213,2,13))
l1 = [10,20,30,40]
print(mySum(*l1))

#dict cafe function -> 메뉴 = 가격 출력해 주는 function
def cafe(**menu):
    for key in menu:
        print(key,"=",menu[key])
    return None
cafe(아메리카노=2000,라떼=3000,핫초코=5000)
print("="*40)
dic = {'아메리카노':1600,'콜드브루':2300,'카페라떼':3500}
cafe(**dic)


