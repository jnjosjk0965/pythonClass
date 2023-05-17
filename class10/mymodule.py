# 나만의 모듈 만들기

def printName(name):
    print("My name is",name)

#import시에 실행되는것을 막기위해 if문사용
if __name__ == "__main__":
    print("오늘은 5월 10일")
    printName("카리나")
    print("축제다!")
    print(__name__)
    
from moduleya.ai import ai
ai.printAI()

import pandas as pd
sl = pd.Series([19,29,123,43],index=["가","나","다","라"])
print(sl.index)
