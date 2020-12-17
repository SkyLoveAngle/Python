#嵌套函数（内部函数）
def outer():
    print("outer running")

    def inner01():
        print("inner01 running")
    inner01()

outer()

def printname(isChinese,name,Fname):
    def inner_print(a,b):
        print("{0}{1}".format(a,b))
    if isChinese:
        inner_print(Fname,name)
    else:
        inner_print(name,Fname)
printname(True,"小七","高")
printname(False,"Ivanka","Trump")

