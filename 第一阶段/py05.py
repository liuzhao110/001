score = int(input("请输入一个0-100之间的分数："))
grade = ''
if score < 0 or score > 100:
    score = int(input("输入错误！请输入一个0-100之间的分数："))
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "不及格"
    print("分数是{0},等级是{1}".format(score, grade))
print("==============================================================================")
score = int(input("请输入0-100之间的分数："))
grade = "ABCDE"
num = 0

if score>100 or score<0:
    score = int(input("输入错误！请输入0-100之间的分数"))
else:
    num = score//10
    if num<6:num=5
    print("分数{0}，等级是{1}".format(score,grade[9-num]))
