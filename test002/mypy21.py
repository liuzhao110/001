import turtle
t = turtle.Pen()
my_colors = ("red","yellow","blue","black","green")
t.width(4)
t.speed(1)
for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(15+i*10)

turtle.done()  # 程序执行完毕后，窗口仍存在
