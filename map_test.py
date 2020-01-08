alist = [1, 2, 3]
blist = [1, 2, 3]
clist = [1, 2, 3]


def add_one(a, b, c):
    return a + b + c


print(list(map(add_one, alist, blist, clist)))
# for i in map(str, alist):
#     print(i)
