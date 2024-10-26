import uuid

from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date =models.DateField()
    availability_status = models.BooleanField(default=True)
    edition = models.CharField(max_length=100 , null=True ,blank=True)
    summary = models.TextField(null=True ,blank= True )


    def __str__(self):
        return self.title