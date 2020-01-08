from threading import Thread, Lock

num = 0
lock = Lock()  # 创建一个互斥锁


def func1():
    lock.acquire()  # 锁上互斥锁，其他线程不能占用
    for i in range(1000000):
        global num
        num += 1
    lock.release()  # 用完资源，解开互斥锁，释放资源给其他
    print(num)


def func2():
    lock.acquire()
    for i in range(1000000):
        global num
        num += 1
    lock.release()
    print(num)


def main():
    print("start")
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end")


if __name__ == "__main__":
    main()