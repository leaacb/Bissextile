from django.db import models


class Archive(models.Model):
    endpoint = models.CharField(max_length=250)
    date = models.CharField(max_length=500)
    result = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.endpoint,self.date}"
