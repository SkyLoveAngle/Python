#形参与实参
def printMax(a,b):
    '''实现两个数的比较，并返回较大的值'''
    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")
printMax(10,20)

#文档字符串（函数的注释，'''三个单引号实现函数注释说明'''）
#调用help函数可以查看函数的文档说明

help(printMax.__doc__)