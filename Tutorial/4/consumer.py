import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')


def callback(ch, method, properties, body):
    print(f'Message - [{body}]')


channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=callback)

channel.start_consuming()
