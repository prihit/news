from django.db import models
from datetime import datetime

# Create your models here
class News(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        db_table = 'News'
    def __str__(self):
        return self.title