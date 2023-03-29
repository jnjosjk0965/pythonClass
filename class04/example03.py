# 문자열 슬라이스
a = "python"
print(a[0], "\t", a[1], "...", a[5])
print("python"[0:2])
print(len(a))

s = "아브라카다브라"
print(s[:5])
print(s[0:3])
print(s[1:4])
print(s[2:4])
print(s[1:])
print(s[-6:])
print(s[0:len(s):2])
ss = "동양미래대학교-컴퓨터소프트웨어공학과"
print(ss[0:len(ss):4])
print(ss[-1:-6:-1])

# 이스케이프 코드
print("hello \n world")
print("hello \t world")
print("hello\b world")
print("hello \v world")