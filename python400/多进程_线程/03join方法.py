from multiprocessing import Process
from time import sleep


def work(interval):
    print("work_start")
    sleep(interval)
    print("work_end")


def work2(interval):
    print("work_start")
    for i in range(interval):
        print(f"工作完成{i+1}")
        sleep(1)
    print("work_over")


def main():
    print("主进程开始")
    p = Process(target=work2, args=(6, ))  # 至今成为work2, 参数为5
    p.start()
    '''调用join方法，主进程要等待join的进程结束再结束'''
    p.join(3)
    """p.join(3)超时时间，时间到，主进程不再等待子进程结束"""
    '''所有进程结束，主进程再执行结束'''
    print("主进程等待结束，over，子进程加班继续")


if __name__ == "__main__":
    main()
