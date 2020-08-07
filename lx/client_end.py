from socket import socket


def main():

    #  创建套接对象
    client = socket()

    # 连接服务器
    client.connect(("10.0.3.203",5800))
    while True:
        data = input("客户端>>>")

        # 向服务器发送消息
        client.send(data.encode("utf-8"))
        if data == 'bey' or data == '拜拜':
            break
    print(client.recv(1024).decode("utf-8"))
    client.close()


if __name__ == '__main__':
    main()
