import pika
import json

def consume_queue(callback):
    conf_connection = pika.ConnectionParameters(
        host='18.234.102.85',
        port=5672,
        credentials=pika.PlainCredentials('testing', 'testing')
    )

    connection = pika.BlockingConnection(conf_connection)
    channel = connection.channel()

    with open('common/config.json', 'r') as f:
        config = json.load(f)

    channel.basic_consume(queue=config["queue"], on_message_callback=callback)

    try:
        print("Waiting messages.....")
        channel.start_consuming()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)







