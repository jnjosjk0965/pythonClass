#7-3 zip
#list, tuple, 문자열 등 여러개를 순서대로 묶어주는것.
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(list(zip(list1,list2)))

# 스포츠 구기종목
sport = ['축구','야구','농구','배구']
num = [11,9,5,6]
sportpn = dict(zip(sport,num))
print(sportpn)
while True:
    name = input("종목이름을 입력하시오.")
    if name in sportpn.keys():
        print(name,"은",sportpn[name],"명이서 하는 스포츠입니다.")
    elif name == "quit" :
        break;
    else:
        print("몰라요")