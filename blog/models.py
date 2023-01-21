from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
class EditBlog(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    text = MDTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "笔记"
        verbose_name_plural = "笔记"

    def __str__(self):
        return self.name
