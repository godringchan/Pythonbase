from multiprocessing import Process, Queue, Manager, pool
# import queue
import time


def write_q(q):
    for i in ["数据1", "数据2", "数据3", "数据4"]:
        q.put(i)
        print("写入数据", i)
        time.sleep(1)


def read_q(q, ):
    while True:
        print(q.get())
        time.sleep(1)


# def main():
#     q = Queue(4)
#     p1 = Process(target=write_q, args=(q, ))


#     p1.start()
#     p2 = Process(target=read_q, args=(q, ))
#     p2.start()
#     # p1.join()
#     p1.kill()
#     p2.join()
def main():
    q = Manager().Queue()
    pool1 = pool.Pool(3)
    pool1.apply_async(write_q, (q, ))
    pool1.apply_async(read_q, (q, ))
    pool1.close()
    pool1.join()


if __name__ == "__main__":
    main()