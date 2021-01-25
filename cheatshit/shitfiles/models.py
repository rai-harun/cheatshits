from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheatShitFor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CheatShits(models.Model):
    cheatshitfor = models.ForeignKey(CheatShitFor, on_delete=models.CASCADE, related_name='cheatshitss')
    heading = models.CharField(max_length=200)
    codes = models.TextField()

    def __str__(self):
        return self.heading
