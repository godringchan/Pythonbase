from threading import Thread, Lock
from time import sleep

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock2.acquire()
lock3.acquire()


class Test1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("...test1...")
                lock2.release()
                sleep(1)


class Test2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("....test2....")
                lock3.release()
                sleep(1)


class Test3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("...test3...")
                lock1.release()
                sleep(1)


def main():
    t1 = Test1()
    t2 = Test2()
    t3 = Test3()
    t1.start()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()