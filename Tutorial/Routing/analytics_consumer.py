import pika
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type=ExchangeType.topic)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(queue=queue_name, exchange='topic_exchange', routing_key='*.europe.*')


def callback(ch, method, properties, body):
    print(f'Analytics Service - message -  [{body}]')


channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

channel.start_consuming()
