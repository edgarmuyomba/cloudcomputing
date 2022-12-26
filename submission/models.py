from django.db import models
from uuid import uuid4

class Confession(models.Model):
    uuidField = models.UUIDField(default=uuid4)
    approved = models.BooleanField(default=False)
    text = models.TextField()
    flag = models.BooleanField(default=False)
    media = models.FileField(upload_to="mediaFiles", null=True, blank=True)

    def __str__(self):
        if len(list(self.text)) > 50:
            return f'{self.text[0:50]}...'
        else: 
            return self.text
