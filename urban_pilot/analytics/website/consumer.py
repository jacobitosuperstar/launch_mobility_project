# website/consumer.py

from django.db.models import F
import os
import sys
import json
import pika
# geolocation package
import pgeocode
from analytics.models import (
    Locations
)


# zone updater
def location_registry(
    zip_code: str,
    operation: str,
    country: str = "US",
):
    try:
        data = pgeocode.Nominatim(country=country)
        data = data.query_postal_code(zip_code)
        city = list(data[["place_name"]])[0]
        county = list(data[["county_name"]])[0]
        state = list(data[["state_name"]])[0]
        location = Locations.objects.get(
            zip_code=zip_code,
            city=city,
            county=county,
            state=state,
        )
        if operation == "add":
            location.users_ammount = F('users_ammount') + 1
        else:
            location.users_ammount = F('users_ammount') - 1
        location.save()
    except Locations.DoesNotExist:
        location = Locations.objects.create(
            zip_code=zip_code,
            city=city,
            county=county,
            state=state,
        )
        location.users_ammount = F('users_ammount') + 1
        location.save()

    response = {
        "message_status": "Processed",
    }
    return response


def consumer(
    host: str,
    port: str,
    queue_name: str,
    routing_key: str,
    exchange: str,
):
    try:
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
        channel.exchange_declare(
            exchange=exchange,
            exchange_type="direct",
        )

        channel.queue_declare(
            queue=queue_name,
            # exclusive=True,
        )

        # queue_name = result.method.queue

        channel.queue_bind(
            queue=queue_name,
            exchange=exchange,
            routing_key=routing_key,
        )

        def callback(ch, method, properties, body):
            payload = json.loads(body)
            print(" [x] Received ")
            info = location_registry(
                zip_code=payload.get("zip_code"),
                operation=payload.get("operation"),
            )
            print(info)

        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
