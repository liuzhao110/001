__author__ = 'liusir'


import  operator
# 先通过sorted 和operator 函数对字典进行排序，然后输出最大value的键
classCount={"c":1,"b":4,"d":2,"e":6}
print(classCount.items())
SortedclassCount1= sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
print(SortedclassCount1[0][0])

# 通过max求字典最大value对应的key
print(max(classCount,key=classCount.get))
print(max(classCount.values()))