from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path("places/", PlaceSearch.as_view(), name="place-search"),
    path("hotels/", HotelSearch.as_view(), name="hotel-search"),
    path("restaurants/", RestaurantSearch.as_view(), name="restaurant-search"),
]
