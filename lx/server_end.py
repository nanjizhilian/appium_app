from socket import socket


def main():

    # 创建套接字对象并指定使用哪种传输协议服务socket（）括号里面不传递参数默认是tcpipv4
    server = socket()

    # 绑定ip地址和端口（这样可以区分不同的服务）端口可以自己指定但是要1024以后的端口
    server.bind(('10.0.3.203',5800))

    #  开启监听-----监听客户端连到服务器
    server.listen(512)

    # 监测服务器是否已经启动
    print("服务器已经启动")

    # 通过循环接收客户端的链接，并做出相应的处理（提供服务）
    while True:

        # 接收客户端的链接accpet是一个阻塞的方法，如果没有客户端连接到服务器
        # 这个方法机会阻塞代码不会向下执行（返回的对象是一个元祖）
        client,addr = server.accept()
        print(str(addr) + '已经成功连到服务器')
        while True:

            #  decode对接收到的消息进行解码
            print(client.recv(1024).decode('utf-8'))
            data = input("服务器>>>")

            # 判断客户端发来的消息，如果出现这种
            if data == '退出聊天' or data == "bey" or data == "拜拜":
                break

            # encode对发送的消息进行解码
            client.send(data.encode("utf-8"))

            # 断开连接
            client.close()


if __name__ == "__main__":
    main()