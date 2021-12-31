from django.db import models
from django.conf import settings

# Create your models here.
class MyText(models.Model) :

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

