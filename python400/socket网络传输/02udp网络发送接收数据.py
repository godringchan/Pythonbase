import socket  # 导入模块
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建udp套接字

# 绑定socket使用端口
udp_s_ip = ("", 8089)
udp_socket.bind(udp_s_ip)
# 对方的（ip地址，端口）
addr = ("10.13.162.61", 8080)
msg = input("发送:")

#利用套接字发送数据

udp_socket.sendto(msg.encode("gbk"), addr)
recv_date = udp_socket.recvfrom(1024)
print(recv_date[0].decode("gbk"))
# 任务结束，关闭套接字
udp_socket.close()