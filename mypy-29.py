#全局变量与局部变量的测试
'''global用于申明全局变量的改变'''
a=3         #全局变量
def test01():
    b=4    #局部变量
    print(b*10)

    a=300
    print(a)

    print(locals())      #打印输出的局部变量
    print(globals())     #打印输出的全局变量

test01()
print(a)

#局部变量和全局变量的效率测试
import math
import time

def test02():
    start = time.time()
    for i in range(1000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}".format((end-start)))

def test03():
    b=math.sqrt
    start = time.time()
    for i in range(1000000):
        b(30)
    end = time.time()
    print("耗时{0}".format((end-start)))