from django.db import models


class Location(models.Model):
    AVAILABLE = 0
    IN_USE = 1
    RESERVED = 2
    UNAVAILABLE = 3
    UNKNOWN = 4
    STATUSES = [
        (AVAILABLE, "AVAILABLE"),
        (IN_USE, "IN_USE"),
        (RESERVED, "RESERVED"),
        (UNAVAILABLE, "UNAVAILABLE"),
        (UNKNOWN, "UNKNOWN"),
    ]
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=11, decimal_places=6)
    lon = models.DecimalField(max_digits=11, decimal_places=6)
    status = models.IntegerField(choices=STATUSES)
    date_created = models.DateTimeField(auto_created=True)
