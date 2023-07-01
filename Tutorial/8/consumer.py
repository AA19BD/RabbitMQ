import random
import time

import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')


def callback(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f'Received - [{body}] with processing time: {processing_time}')
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f'Finished processing')


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='letterbox', on_message_callback=callback)

channel.start_consuming()
