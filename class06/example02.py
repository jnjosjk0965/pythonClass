fruit = ["orange","apple","mango","banana","kiwi"]

print(f"{'sorted 함수 사용':=^40}")
sortedList = sorted(fruit)
print("원본 리스트 : ",fruit)
print("대입 리스트 : ",sortedList)

print(f"{'sort 함수 사용':=^40}")
sortedList = fruit.sort()
print("원본 리스트 : ",fruit)
print("대입 리스트 : ",sortedList)

fruit.clear()

#리스트 컴프리핸션
#리스트를 선언할때, 짧게, 빠르게 간결하게
#0~10까지 숫자가 있는 리스트를 선언
#1 그냥 선언
l1 = [0,1,2,3,4,5,6,7,8,9,10]
#2 for문으로 append
l2 = []
for i in range(11):
    l2.append(i)
#3 리스트 컴프리핸션
l3 = [el for el in range(11)]

# 0~10 까지의 숫자의 제곱을 리스트에 
l4 = [el * el for el in range(11)]
print(l4)
# 0~10 까지의 숫자의 3배수를 리스트에
l5 = [el * 3 for el in range(11)]
print(l5)
# hello 를 10번 넣어라
l6 = ["hello" for i in range(10)]
print(l6)

l7 = list(range(3,6))
print(l7)

# 0~10까지 짝수들의 제곱을 리스트에
# l8 = [el**2 for el in range(2,11,2)]
l8 = [el**2 for el in range(1,11) if el % 2 == 0 ]
print(l8)

# list 복사
a = [ i**2  for i in range(2,11,2)]
b = a
print("a : ", a)
print("b : ", b)

b = a.copy()
print(f"{'after a.copy':=^30}")
print("a : ", a)
print("b : ", b)

a.pop()
print(f"{'after a.pop()':=^30}")
print("a : ", a)
print("b : ", b)

c = a[:]
print(a is c)