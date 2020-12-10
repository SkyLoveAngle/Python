#测试zip()并行迭代

for i in [1,2,3]:
    print(i)

names=("高琪","高二","高三","高四")
ages=(18,26,25,29)
jobs=("老师","程序员","公务员")

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

for i in range(3):
    print("{}--{}--{}".format(names[i],ages[i],jobs[i]))