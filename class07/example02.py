#zip, enumerate()
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
l3 = [6,7,8,9,10]

z = zip(l1,l2,l3)
print(list(z))
print(list(z)) # 한번 사용하면 없어짐
z = zip(l1,l2)
print(dict(z))
z = zip(l1,zip(l2,l3))
print(dict(z))


#문제
#과목을 주면 강의실을 알려주는 시스템
sub = ['파이썬','자바','C++','AI','알고리즘']
roomNum = [101,102,103,104,105]
#1 dictionary로 변환
#2 무한루프를 통해
#3 quit 단어 들어오면 종료
#4 없는 과목을 물어보면 "몰라요"출력

info = dict(zip(sub,roomNum))
print(info)

while True:
    question = input("어떤 과목의 강의실을 알고싶으신가요? : ")
    if question == "quit" :
        break
    else :
        print("찾으시는 강의실은 ",info.get(question,"몰라요."))