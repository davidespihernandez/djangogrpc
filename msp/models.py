from django.db import models


class Token(models.Model):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_created=True)
