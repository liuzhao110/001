for i in range(10):
    print(i,end='\t')
for i in range(3,10):
    print(i,end='\t')
for i in range(3,10,2):
    print(i,end='\t')


sum_all = 0
sum_even = 0
sum_odd = 0
for num in range(101):
    sum_all += num
    print("1-100所有数之和",sum_all)
for num in range(0,101,2):
    sum_even += num
    print("1-100所有偶数之和", sum_even)
for num in range(1,101,2):
    sum_odd += num
    print("1-100所有奇数之和", sum_odd)

sum_all = 0
sum_even = 0
sum_odd = 0
for num in range(101):
    sum_all += num
    if num%2==0:sum_even += num
    else:sum_odd += num
    print("1-100累加之和{0}，偶数之和{1}，奇数之和{2}".format(sum_all,sum_even,sum_odd))