from common.utils import OutgoingMessage, IncomingMessage
from common.consumer import consume_queue
import multiprocessing
from src.v1.layout import DOCUMENT


class app:

    def __init__(self):
        self.message_handler()

    @staticmethod
    def send_message_to_work_queue(contact_name: str, response_message: str, number: str, channel, queue: str):
        data = OutgoingMessage.set_info(contact_name, response_message, number)
        channel.basic_publish(exchange='', routing_key=queue, body=data)
        print(f" [x] Sent\n quee--> {queue}\n' {data}'")

    @staticmethod
    def message_handler():
        def callback(channel, method, properties, body):
            contact_name, payload, number = IncomingMessage.get_info(body)
            payload = payload.upper()
            command = payload.split("\n")
            command_strip = command[0].strip()

            if command_strip == "PRINT":
                data = DOCUMENT.message_to_print(payload)
                app.send_message_to_work_queue(contact_name, data, number, channel, 'responses')
                channel.basic_ack(delivery_tag=method.delivery_tag)
            else:
                payload = "Escriba la palabra help"
                app.send_message_to_work_queue(contact_name, payload, number, channel, 'responses')
                channel.basic_ack(delivery_tag=method.delivery_tag)

        consumer = multiprocessing.Process(target=consume_queue(callback))
        consumer.start()


if __name__ == '__main__':
    app()



