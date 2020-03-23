from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Search(models.Model):
    search_engine = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    keyword = models.CharField(max_length=20)
