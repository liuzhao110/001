r1 = dict(name="搞笑一", age=18, salary=30000, city="北京")
r2 = dict(name="搞笑二", age=19, salary=20000, city="上海")
r3 = dict(name="搞笑三", age=120, salary=10000, city="深圳")
tb = [r1, r2, r3]
for x in tb:
    if x.get("salary") > 15000:
        print(x)
