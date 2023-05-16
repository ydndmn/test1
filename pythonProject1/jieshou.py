import pika,sys,os

def main():
    # 链接到RabbitMQ服务器

    # 输入登陆服务器的用户名和密码
    credentials = pika.PlainCredentials('guest', 'guest')
    # IP地址，端口号，虚拟主机名，用户对象
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # 创建频道
    channel = connection.channel()
    # 声明消息队列,队列名为queue=''单引号中的内容
    channel.queue_declare(queue='hello')
    # 定义接受消息的回调函数
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    # 告诉RabbitMQ使用callback来接收信息
    # queue是要消费的消息队列的队列名，on_message_callback是要使用的回调函数，auto_ack
    # 当autoAck设置为true时，也就是自动确认模式，一旦消息队列将消息发送给消息消费者后，就会从内存中将这个消息删除。
    # 当autoAck设置为false时，也就是手动模式，如果此时的有一个消费者宕机，消息队列就会将这条消息继续发送给其他的消费者，这样数据在消息消费者集群的环境下，也就算是不丢失了。
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    # 开始接收信息
    channel.start_consuming()

if __name__ == '__main__':
    # 一旦检测到键盘中断就会结束程序
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
    # 一旦结束程序就会退出解释器
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
