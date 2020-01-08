from multiprocessing import Process
from time import sleep


def work1(interval):
    print("执行work1")
    sleep(interval)
    print("work1结束")


def work2(interval):
    print("执行work2")
    sleep(interval)
    print("work2结束")


def work3(interval):
    print("执行work3")
    sleep(interval)
    print("work3结束")


def main():
    print("主进程开始")
    p1 = Process(target=work1, args=(5, ))
    p2 = Process(target=work2, args=(3, ))
    p3 = Process(target=work3, args=(1, ))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("主进程结束")


if __name__ == "__main__":
    main()