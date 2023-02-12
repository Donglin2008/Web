from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
class Topic(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Entry(models.Model):
    objects = models.Manager()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    preface = models.TextField()
    text = MDTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.name