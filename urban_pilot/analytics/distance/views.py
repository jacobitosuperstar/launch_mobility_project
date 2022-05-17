# distance/views.py

import json
from django.views.decorators.http import (
    require_POST,
)
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpRequest,
    JsonResponse,
)
from analytics.models import (
    Locations,
)
import pgeocode


def location_distance(
    zip_code_1: str,
    zip_code_2: str,
    country: str = "US",
) -> float:
    """Distance between two zip codes."""
    distance = pgeocode.GeoDistance(country)
    distance = distance.query_postal_code(zip_code_1, zip_code_2)
    return distance


@csrf_exempt
@require_POST
def api_distance_between_locations_view(request: HttpRequest) -> JsonResponse:
    """Distance Measurement"""
    print("MIRAR ACÁ")
    body = request.body
    print(body)
    body = json.load(body)
    print(body)
    print(type(body))
    zip_code_1 = body.get("zip_code_1")
    zip_code_2 = body.get("zip_code_2")
    distance = location_distance(
        zip_code_1=zip_code_1,
        zip_code_2=zip_code_2,
    )
    info = {
        "status": 200,
        "distance [km]": distance,
    }
    return JsonResponse(info)

