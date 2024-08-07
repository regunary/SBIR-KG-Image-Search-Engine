from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title