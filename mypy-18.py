#break语句和continue语句的测试

while True:
    a=input("请输入一个字符（输入Q或q时退出）：")
    if a=="Q" or a=="q":
        print("循环结束，退出循环。")
        break
    else:
        print("你输入的是：",a)

