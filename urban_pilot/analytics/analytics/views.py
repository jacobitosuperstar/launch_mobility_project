from django.views.decorators.http import (
    require_GET,
)
from django.http import (
    HttpRequest,
    JsonResponse,
)
from .models import (
    Locations,
)

from threading import Thread
from website.consumer import consumer

consumer_variables = {
    "host": "rabbitmq",
    "port": "5672",
    "queue_name": "location_tracker",
    "routing_key": "user.location.tracker",
    "exchange": "location.tracker",
}
thread = Thread(target=consumer, kwargs=consumer_variables)
thread.setDaemon(True)
thread.start()


@require_GET
def api_ordered_locations_view(request: HttpRequest) -> JsonResponse:
    """Ordered Locations by user ammount"""
    locations = Locations.objects.all().order_by("users_ammount")
    locations_list = [{
        "zip_code": location.zip_code,
        "city": location.city,
        "county": location.county,
        "state": location.state,
        "users_ammount": location.users_ammount,
    } for location in locations]
    info = {
        "status": 200,
        "locations": locations_list,
    }
    return JsonResponse(info)
