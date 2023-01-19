from django.conf import settings
from django.db import models
class Subscription(models.Model):
    'Generated Model'
    name = models.CharField(max_length=50,)
    price = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True,)
    description = models.TextField(null=True,blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)

# Create your models here.
