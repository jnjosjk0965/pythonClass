from datetime import datetime
import random
#조건문 
now = datetime.now()
if now.hour < 12 :
    print("오전")
elif now.hour == 12:
    print("정오")
else :
    print("오후")
    
isLunch = input("밥 먹을래?")
if isLunch == "yes" :
    print("그래 먹자")
    food = input("뭐 먹지 학식 먹을래?")
    if food == "yes" : 
        print("그래 역시 학식만한게 없지~")
    else : 
        print("그래 역시 학식은 걸러야지~")
        food = input("그럼 써브웨이?")
        if food == "yes" :
            print("지하철 가자")
        else : 
            print("이걸 거르네")
else :
    print("그래 니 몸무게에 밥이 넘어가냐")
    
#for, while
for i in range(-20,10,3) :
    print(i)
    
sum = 0
for n in range(1,11) :
    sum += n
print(sum)

array = [1,2,3,5,7,11,13,17,19,23,29]
sum = 0
for n in array:
    sum += n
else: # for문이 정상 종료시
    print(sum)
    
# while
lcv = 0
while lcv < 10:
    print(lcv,end=" ")
    lcv += 1

# break continue
# 단어입력을 무한으로 받음
# 받은 단어를 3번 출력
# "exit"  작성시 루프 탈출
# "apple" -> 3번 출력x 다시 입력으로

while True:
    voca = input("단어를 입력하세요 : ")
    if(voca == "exit"):
        print("긴급 탈출")
        break
    elif(voca == "apple"):
        continue
    print(voca * 3)
    
ranNum = random.randint(0,10)
print(ranNum)