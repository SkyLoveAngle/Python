#参数的传递
#可变对象
a=[10,20]
print(id(a))
print(a)
print("*"*50)

def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))

test01(a)
print(a)

#参数是不可变对象
print("*"*50)
a=100
def f1(n):
    print("n:",id(n))
    n=n+200
    print("n:",id(n))
    print(n)
f1(a)
print("a:",id(a))