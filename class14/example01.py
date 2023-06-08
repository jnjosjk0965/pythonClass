# dictionary
# key : 자동차 등록번호 , value : (생산년도, 배기량)
carDict = { 'h101' : ('2021','2000'),'h102' : ('2021','2000'),
            'b101' : ('2020','3600'),'b102' : ('2021','4200')}
keys = carDict.keys()
values = carDict.values()
items = carDict.items()


for key in keys:
    print(key,carDict[key])
    
print("="*30)
# 다른 방법
for item in items:
    print(item[0],item[1])
    
yearList = []
for value in carDict.values():
    yearList.append(int(value[0]))
print(yearList)

searchYear = int(input("생산년도를 입력하시오 : "))
print(searchYear,"년에 생산된 자동차는",yearList.count(searchYear), "대 있습니다.")

members = { '홍':'111','박':'222','정':'333'}
members['최'] = '555'
members.update({'강':'666'})
members['김'] = '777'
members.update({'최':'888'})
print(members)