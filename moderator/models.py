from django.db import models
from uuid import uuid4

class Advert(models.Model):
    uuid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    description = models.TextField()
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
