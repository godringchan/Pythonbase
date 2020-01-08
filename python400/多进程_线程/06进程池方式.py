import multiprocessing
import time


def func():
    for i in range(5):
        print(f"func开始执行{i}")
        time.sleep(1)


def func1():
    for i in range(5):
        print(f"func1开始执行{i}")
        time.sleep(1)


def func2():
    for i in range(5):
        print(f"func2开始执行{i}")
        time.sleep(1)


def func3():
    for i in range(5):
        print(f"func3开始执行{i}")
        time.sleep(1)


'''进程池，一次放一类的函数
p_pool.apply_async(func, (interval, )),
可以传入函数的变量为一个元组,async是异步(解开堵塞),
不同函数要添加到进程池，需要多执行添加操作或者放在列表中用for添加，由进程池管理进程执行顺序'''


def main():
    print("主进程开始")
    p_pool = multiprocessing.Pool(2)
    print(id(p_pool))
    p_pool.apply_async(func)
    p_pool.apply_async(func1)
    p_pool.apply_async(func2)
    p_pool.apply_async(func3)
    p_pool.close()
    p_pool.join()
    print(id(p_pool))
    print("主进程结束")


if __name__ == "__main__":
    main()
