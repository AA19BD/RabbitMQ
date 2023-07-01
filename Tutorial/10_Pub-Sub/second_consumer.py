import pika
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(queue=queue_name, exchange='pubsub')


def callback(ch, method, properties, body):
    print(f'Second Consumer message - [{body}]')


channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

channel.start_consuming()
