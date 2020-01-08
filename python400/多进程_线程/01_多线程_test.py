from time import sleep


def dance():
    for i in range(3):
        print("跳一支舞")
        sleep(1)
        sing()


def sing():
    for i in range(3):
        print("唱一首歌")
        sleep(1)


if __name__ == "__main__":
    dance()
    # sing()