from django.db import models

# Create your models here

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn = models.CharField(max_length=13,unique=True)
    description=models.TextField(blank=True)
    publish_year = models.PositiveIntegerField(null=True,blank=True)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title