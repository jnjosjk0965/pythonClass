# 놀이동산 놀이기구
# 정원 4명
# 정원이 차면 시작
# 조건 키 150 이상
# 탑승시 키를 물어봄

count = 0
while count < 4 :
    height = int(input("키가 몇인가요?"))
    if height >= 150 :
        count += 1
else:
    print("놀이기구 시작!")