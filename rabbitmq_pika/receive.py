# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

# connect to broker on localhost or external IP address and get a channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created
channel.queue_declare(queue='hello')


# Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue.
# Whenever we receive a message, this callback function is called by the Pika library. In our case this function
# will print on the screen the contents of the message.
def callback(ch, method, properties, body):
    print(" [x] received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print('[*] Waiting for messages. To exit pres Ctrl+C')

# enter a never-ending loop that waits for data and runs callbacks whenever necessary
channel.start_consuming()
