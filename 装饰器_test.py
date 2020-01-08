def fun_add(fun):  # 装饰器是一个闭包,主要作用是把主函数传递到内部函数,进行调用并添加新功能,并返回内部函数
    print("装饰器1")

    def fun_add_1():

        print("附加功能1")
        fun()

    return fun_add_1


def fun_add2(fun):
    print("装饰器2")

    def fun_add_2():

        print("附加功能2")
        fun()

    return fun_add_2


@fun_add
@fun_add2
def fun1():
    print("功能一")


if __name__ == "__main__":

    fun1()