# filter 把列表元素传入一个判断返回true,和flase的函数中, true被保留,flase会删除

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(x):  # 判断时候双数的函数
    return x % 2 == 0


blist = filter(func, alist)

print(list(blist))