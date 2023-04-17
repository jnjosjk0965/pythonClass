#0412
# 빈리스트를 만들어 하나씩 원소 추가
foodList = []
foodList.append("피자")
foodList.append("카레")
foodList.append("돈까스")
foodList.append("치킨")
print(foodList)
foodList.insert(1,"샌드위치")
foodList.append("치킨")
foodList.append("카레")
foodList.append("치킨")
foodList.append("치킨")
foodList.append("카레")
foodList.append("치킨")

print(foodList)
print("="*20)
for i in range(len(foodList)):
    print(foodList[i])
print("="*20)
for item in foodList:
    print(item)
    
print(foodList.count("치킨"),foodList.index("치킨"))

print(foodList[0:8:2])

deleteEl = input("지울 음식을 입력 : ")

if deleteEl in foodList:
    foodList.remove("치킨")
    print(deleteEl,"정상적으로 삭제됨")
else:
    print(deleteEl,"존재하지 않음")
print(foodList)

foodList.pop()

dessert = ["케이크","와플","마카롱"]
foodList.extend(dessert)
print(foodList)
