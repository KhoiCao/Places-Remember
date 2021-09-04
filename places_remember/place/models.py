from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Memory(models.Model):
    memory_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.memory_name
        