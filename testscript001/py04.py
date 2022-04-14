x = int(input("请输入坐标X："))
y = int(input("请输入坐标Y："))
if x == 0:
    print("Y轴")
elif y == 0:
    print("X轴")
elif x > 0 and y > 0:
    print("第一象限")
elif x < 0 and y > 0:
    print("第二象限")
elif x < 0 and y < 0:
    print("第三象限")
else:
    print("第四象限")
