# num = 0
# while num<=10:
#     print(num,end='\t')
#     num +=1

num = 0
sum_all = 0
sum_even = 0
sum_odd = 0
while num<=100:
    sum_all = sum_all + num
    if num%2==0:sum_even += num
    else:sum_odd +=num
    num += 1   #迭代，改变条件表达式，使循环趋于结束
    print("1-100所有数的累加和",sum_all)
    print("1-100所有偶数的累加和",sum_even)
    print("1-100所有奇数的累加和",sum_odd)


