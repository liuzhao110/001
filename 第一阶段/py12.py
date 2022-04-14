empNum = 0
salarySum = 0
salarys = []
for i in range(4):
    s = input("请输入一共4名员工的薪资（按Q或q中途结束）")
    if s.upper()=="Q":
        print("录入完成，退出")
        break
    if float(s)<0:
        print("薪资小于0，请重新输入")
        continue
    empNum +=1
    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已全部录入4名全部员工的薪资")

print('员工数{0}'.format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))
