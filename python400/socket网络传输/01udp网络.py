import socket
# 生成套接字
Udp_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对方的ip地址与接收端口
addr = ("10.13.162.61", 8080)
msg = input("发送:")
# 发送数据
Udp_Socket.sendto(msg.encode("gbk"), addr)
# 关闭套接字
Udp_Socket.close()