import pika
from pika.exchange_type import ExchangeType


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type=ExchangeType.topic)
user_payments_message = 'European user paid!'

# for key in ['analytics_only', 'payments_only']:
channel.basic_publish(exchange='topic_exchange', routing_key='user.europe.payments', body=user_payments_message)
# channel.basic_publish(exchange='routing', routing_key='both', body=message)

print(f'Sent message: [{user_payments_message}]')

connection.close()