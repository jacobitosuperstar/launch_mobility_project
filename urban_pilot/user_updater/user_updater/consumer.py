# user_updater/consumer.py

import os
import sys
import json
import pika
# geolocation package
import pgeocode
from .models import User
from user_updater import db


# zone updater
def geolocater(
    user_id: int,
    zip_code: str,
    country: str = "US",
):
    data = pgeocode.Nominatim(country=country)
    data = data.query_postal_code(zip_code)
    city = list(data[["place_name"]])[0]
    county = list(data[["county_name"]])[0]
    state = list(data[["state_name"]])[0]
    user = User.query.filter_by(id=user_id).first()
    if user:
        if city:
            user.city = city
        if county:
            user.county = county
        if state:
            user.state = state
        db.session.add(user)
        db.session.commit()
        user = [{
            "id": user.id,
            "firt_name": user.first_name,
            "middle_name": user.middle_name,
            "last_name": user.last_name,
            "email": user.email,
            "zip_code": user.zip_code,
            "city": user.city,
            "county": user.county,
            "state": user.state,
        }]
    response = {
        "message_status": "Processed",
        "user": user,
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
                #     'usuariocsj',
                #     'usuariocsj'
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
            info = geolocater(
                user_id=payload.get("user").get("id"),
                zip_code=payload.get("user").get("zip_code"),
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
