import socket
# 创建一个tcp套接字
custermer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取要连接的客户端的ip
server_addr = ("10.13.162.61", 8989)
# 客户端链接服务器
custermer_socket.connect(server_addr)
while True:

    msg = input("告诉对方:")
    custermer_socket.send(msg.encode("gbk"))
    recv_data = custermer_socket.recv(1024)
    print(recv_data.decode("gbk"))

custermer_socket.close()