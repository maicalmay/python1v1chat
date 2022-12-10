import socket

# 定义服务器ip、端口
print("请定义本机IP:")
ip = input()
ip_ad=(ip,9999)

# 创建socket对象
sk=socket.socket()

# 绑定ip端口
sk.bind(ip_ad)

# 开启监听
sk.listen()
print('服务器已经开启......')

# 等待接收客户端信息
conn,addr=sk.accept()
print('客户端地址:',addr)


while True:
# 等待接收客户端信息，接收到信息并非是字节格式，所以需要解码才能被正常识别【decode('utf-8')】
    cli_data=conn.recv(1024).decode('utf-8')
    print('对方:',cli_data)#对方

# 发送信息给客户端，发送的信息非字节格式，需要先转换格式【encode('utf-8'))】
    sen_data=input('~#:')
    conn.sendall(sen_data.encode('utf-8'))

sk.close()