#测试while循环
num =0
while num<10:
    num+=1
    print(num,end="\t")
print("**************************")

#计算1-100之间的数字累加和,奇数项累加和，偶数项累加和
num2=0
sum_all =0
sum_even = 0
sum_odd = 0

while num2<=100:
    sum_all = sum_all + num2
    if num2 % 2 == 0:
        sum_even = sum_even + num2
    else:
        sum_odd = sum_odd + num2

    num2+=1
print("1-100之间的所有数字累加和为：" ,sum_all)
print("1-100之间的所有奇数项累加和为：" ,sum_even)
print("1-100之间的所有偶数项累加和为：" ,sum_odd)