from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path("places/", PlaceList.as_view(), name="place-list"),
    path("places/search/", PlaceSearch.as_view(), name="place-search"),
    path("hotels/", HotelList.as_view(), name="hotel-list"),
    path("hotels/search/", HotelSearch.as_view(), name="hotel-search"),
]
