x=int(input("请输入X的坐标"))
y=int(input("请输入Y的坐标"))

if(x==0 and y==0):
    print("原点")

elif(x==0):
    print("Y轴")

elif(y==0):
    print("X轴")

elif(x>100 and y>0):
    print("第一象限")

elif(x<0 and y>0):
    print("第二象限")

elif(x<0 and y<0):
    print("第三象限")

elif(x>0 and y<0):
    print("第四象限")
