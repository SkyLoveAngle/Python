r1={"name":"高一","age":"18","salary":"3000","city":"北京"}
r2={"name":"高二","age":"19","salary":"4000","city":"上海"}
r3={"name":"高三","age":"20","salary":"5000","city":"广州"}
tb=[r1,r2,r3]
#获高小二的薪资
print(tb[1].get("salary"))
#获取表中所有人的薪资
for i in range(len(tb)):#i--->0 1 2
    print(tb[i].get("salary"))
#打印所有的数据
for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("salary"),tb[i].get("city"))
