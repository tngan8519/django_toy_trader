from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Toy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rent_price = models.CharField(max_length=200)
    sale_price = models.CharField(max_length=200)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name