# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

# connect to broker on localhost or external IP address and get a channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# create a queue, if it doesn't exist pika drops the message
channel.queue_declare(queue='hello')
# routing_key param declares the queue to which message is passed
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Silver Surfer')

# Print to terminal
print('Said "Silver Surfer"')

# close the connection
connection.close()
