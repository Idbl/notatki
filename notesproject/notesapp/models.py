from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(db_column='title', max_length=50, blank=False)
    content = models.CharField(db_column='content', max_length=1000)
    creation_date = models.DateTimeField(db_column='creation_date')
    author = models.CharField(db_column='author', max_length=1000, blank=False)

