# users/producer.py

import json
import pika


def rabbit_mq_sender(
    message: dict,
    host: str,
    port: int,
    queue_name: str,
    routing_key: str,
    exchange: str,
    # virtual_host: str
) -> dict:
    """
    Function for direct connection with the RabbitMQ tail.

    Args =>

    message: dict -> Message to send.

    host:str -> IP of the connection of Rabbit in string form.

    port: str -> Port number (add it as a string) of the host we are connecting
                 to.

    queue_name: str -> Name of the queue.

    routing_key: str -> Name of the route

    exchange: str -> Name of the exchange
    """
    message = json.dumps(message)

    # creando la señal de envío del objeto/mensaje a RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            port=port,
            # virtual_host=virtual_host,
            # credentials=pika.PlainCredentials(
            #     '',
            #     ''
            # )
        )
    )
    channel = connection.channel()
    channel.queue_declare(
        queue=queue_name
    )
    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(
            content_type='text/plain'
        )
    )
    connection.close()
    return None
