import threading
import time


def func1(name, sec):
    print(f"{name}正在运行")
    time.sleep(sec)
    print(f"{name}结束")


def func2(name, sec):
    print(f"{name}正在运行")
    time.sleep(sec)
    print(f"{name}结束")


class MyThread(threading.Thread):
    def __init__(
            self,
            func,
            name,
            args,
    ):
        super().__init__(target=func, name=name, args=args)

    def run(self):
        # return super().run()
        self._target(self.name, *self._args)


def main():
    print("开始运行")
    t1 = MyThread(func1, "线程1", (5, ))
    t2 = MyThread(func2, "线程2", (2, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("程序结束")


if __name__ == "__main__":
    main()