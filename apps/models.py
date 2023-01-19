from django.conf import settings
from django.db import models
class Application(models.Model):
    'Generated Model'
    name = models.CharField(max_length=50,)
    description = models.TextField(max_length=256,null=True,blank=True,)
    type = models.CharField(max_length=50,null=True,blank=True,)
    framework = models.CharField(max_length=50,null=True,blank=True,)
    domain_name = models.CharField(max_length=50,null=True,blank=True,)
    screenshot = models.URLField(null=True,blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,)

# Create your models here.
