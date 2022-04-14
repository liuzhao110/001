def printMax(a,b):
    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")

printMax(10,20)
printMax(10,3)

def print_star(n):
    '''根据输入的n，打印多个星号'''
    print("*"*n)
help(print_star)


def print_see(n):
    print("*"*n)

print_see(5)

def my_avg(a,b):
    return(a+b)/2
print(my_avg)
print(id(my_avg))
c = my_avg(10,20)
print(int(c))

