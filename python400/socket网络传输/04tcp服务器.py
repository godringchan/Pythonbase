import socket

# 创建一个tcp的socket套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp服务器必须绑定一个ip与端口
tcp_socket.bind(("", 8989))
# listen方法启动socket监听用户
tcp_socket.listen(5)
# accpet方法堵塞程序,等待客户的链接,当客户链接会返回一个元组(客户端套接字, 客户端的ip地址)
custermer_socket, custermer_addr = tcp_socket.accept()
# print(custermer_socket)
# 变量接收accpet返回的客户套接字,使用客户套接字与客户进行链接
cus_recv_data = custermer_socket.recv(1024)
print(cus_recv_data.decode("gbk"))

# 任务结束,关闭客户套接字,与服务器套接字,一般服务器长期开机,不会关闭.但必须关闭客户套接字,释放资源
custermer_socket.close()
tcp_socket.close()