num = input("请输入数字：")
if int(num)<10:
    print(num)
else:
    print("数字太大")


num = input("请输入数字1：")
print(num if int(num)<10 else "数字太大")