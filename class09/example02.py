#lambda function
def add4(num):
    return num + 4
# 위 함수를 lambda func로
print((lambda num:num+4)(100))
#숫자 입력받아서 10곱
print((lambda num:num*10)(43))
#숫자2개 입력 받아서 서로곱
print((lambda num1,num2:num1*num2)(32,4))

#map, filter
#map(function,list)=> return list
list1 = list(map(lambda num:num*2,[1,2,3,4]))
print(list1)

# 5배를 하고 10을 더해서 결과를 리스트로 풀력
list2 = [1,2,3,4,5,6]
result1 = list(map(lambda num:num*5+10,list2))
print(result1)

#두개의 리스트를 하나씩 뽑아서 두개를 더해 새로운 리스트
li1 = [10,20,30,40,50]
li2 = [1,2,3,4,5]
result2 = list(map(lambda n1,n2:n1+n2,li1,li2))
print(result2)

#filter(function,list)=> lsit
list3 = [12,-3,4,-9,32]
result3 = list(filter(lambda n:n>0,list3))
print(result3)