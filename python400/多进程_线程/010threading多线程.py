import threading
import time


def func(func_name, delay):
    print(f"{func_name}正在执行")
    time.sleep(delay)
    print(f"{func_name}执行结束")


def func2(func_name, delay):
    print(f"{func_name}正在执行")
    time.sleep(delay)
    print(f"{func_name}结束")


def main():
    t1 = threading.Thread(target=func, args=("线程1", 5))
    t2 = threading.Thread(target=func2, args=("线程2", 3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()