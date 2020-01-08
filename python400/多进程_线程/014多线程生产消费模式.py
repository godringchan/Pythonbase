import threading
import queue
import time

# 全局队列，放在主线程中
# q = queue.Queue()


# 生产
def producter():
    global q
    count = 0
    while True:
        if q.qsize() < 500:
            for i in range(100):
                count += 1
                msg = f"第{count}个产品"
                q.put(msg)
                print("生产了" + msg + f"库存为{q.qsize()}")
        time.sleep(1)


# 消费
def custermer():
    global q
    while True:
        if q.qsize() >= 500:
            for i in range(300):
                print(f"消费了{q.get()},库存为{q.qsize()}")
        time.sleep(1)


# 主线程
def main():
    t1 = threading.Thread(target=producter)
    t2 = threading.Thread(target=custermer)
    t1.start()
    t2.start()


if __name__ == "__main__":
    # 全局变量，队列q
    q = queue.Queue()
    main()