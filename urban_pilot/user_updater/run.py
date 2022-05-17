from user_updater import app
from user_updater import db
# consumer
import pika
from user_updater.consumer import consumer
# threads
from threading import Thread


# start thread where the consumer is going to start
consumer_variables = {
    "host": "rabbitmq",
    "port": "5672",
    "queue_name": "user_updater",
    "routing_key": "user.information.updater",
    "exchange": "information.updater",
}
thread = Thread(target=consumer, kwargs=consumer_variables)
thread.setDaemon(True)
thread.start()
# end of the consumer thread


if __name__ == "__main__":
    db.create_all()
    app.run(
        host='0.0.0.0',
        port='5000',
        debug=True,
        threaded=True
    )
