import socket
import threading


def send_msg():
    while True:
        msg = input("消息:")
        udp_socket.sendto(msg.encode("gbk"), other_addr)


def rec_msg():
    while True:
        udp_rec_msg = udp_socket.recvfrom(1024)
        if udp_rec_msg:
            print(udp_rec_msg[0].decode("gbk"))


def main():
    try:
        send_th = threading.Thread(target=send_msg)
        rec_th = threading.Thread(target=rec_msg)
        send_th.start()
        rec_th.start()
        rec_th.join()
    finally:
        udp_socket.close()
        print("关闭套接字")


if __name__ == "__main__":
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8089))
    other_addr = ("10.13.162.61", 8080)

    main()
