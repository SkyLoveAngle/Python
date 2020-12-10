#绘制同心圆
import turtle
t =turtle.Pen()

my_colors=("yellow","green","blue","red","orange")

t.width(4)
t.speed(0)
for i in range(100):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(15+i*10)

turtle.done()   #程序执行完，窗口仍然在