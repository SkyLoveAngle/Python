#列表推导式
a=[x for x in range(1,5)]
b=[x*2 for x in range(1,5)]
c=[x*2 for x in range(1,20)if x%5==0]
print(a)
print(b)
print(c)
#下面for循环实现同样功能
y=[]
for x in range (1,50):
    if x%5==0:
        y.append(x*2)
print(y)

d=[x for x in "abcdefg"]
print(d)

cells=[(row,col) for row in range(1,10) for col in range (1,10)]
for cell in cells:
    print(cell)

#字典推导式
my_text = "i love you,i love sxt,i love gaoqi"
char_count={x:my_text.count(x) for x in my_text}
print(char_count)
#使用普通for循环实现上面的字典推导式实现的字符出现的次数统计


#集合推导式
e={x for x in range(1,100) if x%9==0}
print(e)

#生成器推导式
gnt=(y for y in range(4))
print(tuple(gnt))

gnt=(x for x in range(1,100) if x%9 ==0)
for x in gnt:             #生成器是一个可迭代的对象
    print(x,end="，")
