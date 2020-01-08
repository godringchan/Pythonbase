import multiprocessing
from time import sleep
import queue


def dance(q):
    for i in range(3):
        print("跳一支舞")
        sleep(1)
        q.put(i)


def sing(q):
    for i in range(3):
        print("唱一首歌")
        sleep(1)
        print(q.get())


def main():
    q = queue.Queue(3)
    print("测试开始")
    p = multiprocessing.Process(target=dance, args=(q, ))
    p1 = multiprocessing.Process(target=sing, args=(q, ))
    p.start()
    p.join()
    p1.start()
    p1.join()


if __name__ == "__main__":
    main()
