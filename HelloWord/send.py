import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 5672(AMQP(RabbitMQ))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='test')

print(" [x] Sent 'Hello World!'")

connection.close()
