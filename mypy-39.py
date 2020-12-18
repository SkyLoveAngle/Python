#nonlocal,global关键字
def outer():
    b=10
    def inner():
        nonlocal  b           #申明外部函数的局部变量
        print("inner b:",b)
        b=20

        global a              #申明全局变量
        a=1000

    inner()
    print("outer b:",b)
outer()
print("outer b:",a)
