import multiprocessing
import time


def clock(interval):
    for i in range(3):
        print(f"当前时间为{time.ctime()}")
        time.sleep(interval)


def main():
    p = multiprocessing.Process(target=clock, args=(3, ))
    p.start()
    '''加入join，主进程等待子线程结束，再继续执行join后面的内容'''
    p.join()
    print("p.pid:", p.pid)
    print("p.name:", p.name)
    print("p.is_alive:", p.is_alive())
    print("主线程结束")


if __name__ == "__main__":
    main()