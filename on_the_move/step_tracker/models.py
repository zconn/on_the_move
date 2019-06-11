from django.db import models
from django.contrib.auth.models import User

class Steps(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(blank=False)
    activitiy = models.TextField(blank=True)
    minutes = models.IntegerField(blank=True)
    steps = models.IntegerField(blank=False)

    def __str__(self):
        return self.entry_date