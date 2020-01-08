"""使用类的方式写多进程，类要继承processing,重写run方法"""
from multiprocessing import Process
import time


class CLockPro(Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):

        print("至今成开始")
        print("开始时间:", time.ctime())
        time.sleep(self.interval)
        print("结束时间:", time.ctime())


def main():
    print("主进程开始")
    p = CLockPro(3)
    p.start()
    p.join()
    print("主进程结束")


if __name__ == "__main__":
    main()