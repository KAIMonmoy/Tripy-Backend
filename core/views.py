from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.serializers import *


class HotelList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class HotelFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="average_rating", lookup_expr='gte')

    class Meta:
        model = Hotel
        fields = [
            'name',
            'place',
            'address',
            'allows_free_cancellation',
            'allows_pay_at_stay',
            'allows_special_offers',
            'has_free_wifi',
            'has_free_parking',
            'has_restaurant',
            'has_pool',
            'has_ac',
            'min_price',
            'max_price',
            'min_rating'
        ]


class HotelSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter
