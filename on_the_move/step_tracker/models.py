from django.db import models
from django.contrib.auth.models import User

class Steps(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(blank=False)
    activitiy = models.TextField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    steps = models.IntegerField(blank=False)

    class Meta:
        verbose_name_plural = "Steps"

    def __str__(self):
        return str(self.author) + " " + str(self.entry_date)
