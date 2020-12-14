#递归函数
def test01(n):
    print("test01:",n)
    if n==0:
        print("OVER")
    else:
        test01(n-1)
    print("test01:******",n)

test01(4)
