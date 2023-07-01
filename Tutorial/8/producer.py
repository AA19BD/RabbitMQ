import time
import random

import pika


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox', )

id = 1
while True:
    message = f'message id - {id}'
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    print(f'Sent message: [{message}]')
    time.sleep(random.randint(1, 3))
    id += 1
