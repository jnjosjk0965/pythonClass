#0510
import random

for i in range(2):
    randnum = random.randint(0,10)
    print(randnum)

import math as m #별명 붙이기

print(m.fsum([2,315,6,41,24,1,1,23,12,3,123,1,23,1,23,12,3,1]))
print(m.pow(2,8))

from math import log10 as l10
print(l10(32031))

import mymodule as my
print("-="*25)
my.printName("재석")

#실행한 곳에서만 __name__에 __main__이 들어가고 아니면 파일명이 들어감
print(__name__)

