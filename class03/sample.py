#2023-03-22
'''이것은 
여러줄 짜리
주석입니다.'''
print("hello world")
print("hello world2")
print(type("hello"))

print(2)
print(type(2))
print(5.5)
print(type(5.5))

print("hello" + "python")
print("===" * 5)

print("hello", "great", "python")
print()

print(1,2,-5,3.14,2.71828)
print('23000원은', '5000원 ?개', '1000원 ?개')
print('5000원', 23000 // 5000,'개')
print('1000원',(23000%5000)//1000,'개')

val = '3+8'
print(eval(val))
print(val)

print(1 + 62 - 3 * 52)
print(256 * 553 - 152)
print(1123123123123123123 % 539253 + 1123123123123123123 // 539253)

'''지불 금액이 78000 5만원 1만원 5000원 지폐로 지불하고 잔돈 얼마?'''
temp = 78000
print("78000원은 5만원권", temp // 50000, '개')
temp %= 50000
print("1만원권은", temp // 10000,"개")
temp %=10000
if temp % 5000 == 0:
    print("5000원권은",temp // 5000)
else:
    rest = temp // 5000 + 1
    print("5000원권은",rest,'개에 거스름 돈으로 ',rest*5000 - temp, '원을 받으면 됩니다.')