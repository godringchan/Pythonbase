from functools import reduce

alist = [1, 3, 5, 8, 9]


def func(x, y):
    return x * 10 + y


# reduce 把列表中的前两元素作为参数传递给函数,获得的结果成为第一元素,和下一个元素进行传递,到列表结束
print(reduce(func, alist))