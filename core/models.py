from django.db import models


class Place(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    # Deals
    allows_free_cancellation = models.BooleanField(blank=True, default=False)
    allows_pay_at_stay = models.BooleanField(blank=True, default=False)
    allows_special_offers = models.BooleanField(blank=True, default=False)
    # Amenities
    has_free_wifi = models.BooleanField(blank=True, default=False)
    has_free_parking = models.BooleanField(blank=True, default=False)
    has_restaurant = models.BooleanField(blank=True, default=False)
    has_pool = models.BooleanField(blank=True, default=False)
    has_ac = models.BooleanField(blank=True, default=False)
    # Prices
    price = models.FloatField()
    # Ratings
    total_ratings = models.PositiveIntegerField(blank=True, default=0)
    average_rating = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=63)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    is_vacant = models.BooleanField(blank=True, default=True)
    booked = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.hotel.name} | {self.number}"