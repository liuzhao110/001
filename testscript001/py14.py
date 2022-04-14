names = ("告诉","房间打开","分阶段","x打开")
ages = ("12","32","12","23")
jobs = ("IT","回答","开发","ceshi")
for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}---{2}".format(name,age,job))