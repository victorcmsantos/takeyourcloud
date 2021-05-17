import pika
import os

credentials = pika.PlainCredentials('nova', 'password')
parameters = pika.ConnectionParameters(host='201.44.3.117', port=int('30360'), virtual_host='nova', credentials=credentials)

def testconn():
  try:
    connection = pika.BlockingConnection(parameters)
    if connection.is_open:
      print('RabbitMQ está rodand')
      connection.close()
      return True
  except Exception as error:
    print('Rabbitmq - mensagem de erro: %s' % error)
    return False
  

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='helloqueue')

channel.basic_publish(exchange='', routing_key='helloroutingkey', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

  
  
  
  
  
  
  
  
