# 测试局变量是否共享
import multiprocessing

num = 10


def work1():
    global num
    num += 10
    print(f"work1结束num={num}")


def work2():
    global num
    num += 3
    print(f"work2结束num={num}")


def main():
    print("主进程开始")
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"全部运行结束num={num}")


if __name__ == "__main__":
    main()