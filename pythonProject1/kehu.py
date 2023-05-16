import time
import pika
import threading
import sys
import os

# 链接到RabbitMQ服务器
# 输入登陆服务器的用户名和密码
credentials = pika.PlainCredentials('guest', 'guest')
# IP地址，端口号，虚拟主机名，用户对象
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

def func(name):
    # 创建频道
    channel = connection.channel()
    # 声明消息队列,队列名为queue=后的内容
    channel.queue_declare(queue=name)
    while True:
        time.sleep(3)
# routing_key是队列名 body是要插入的内容，routing_key和上面的queue中的内容要一致
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
# 关闭链接，释放资源

if __name__ == '__main__':
# 定时器，（间隔时间，运行的函数）
    try:
        threading.Timer(1, func('hello')).start()
    except KeyboardInterrupt:
        connection.close()
        print('Interrupted')
    # 一旦结束程序就会退出解释器
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)