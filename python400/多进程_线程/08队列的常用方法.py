'''queue已经不在multiprocessing模块中'''
import queue

q = queue.Queue(3)  # 创建队列，设置队列空间3
q.put("数据1")
q.put("数据2")
q.put("数据3", block=True, timeout=1)  # block=True,当队列满了，
# 使用put不等待timeout后会报错

if not q.full():
    q.put("数据4")
print(f"获取第一个{q.get()}")
if not q.empty():
    print(f"还有{q.qsize()}个数据")
    for i in range(q.qsize()):  # q.qsize()获取队列中数据数目
        print(q.get(block=True, timeout=1))