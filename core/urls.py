from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path("hotels/", HotelList.as_view(), name="hotel-list"),
    path("hotels/search/", HotelSearch.as_view(), name="hotel-search"),
]
