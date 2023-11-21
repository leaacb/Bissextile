from django.db import models

class Year(models.Model):
    value = models.IntegerField()

    def bissextile(self):
        isbissextile = False
        if (self.value % 4 == 0 and self.value % 100 == 0 and self.value % 400 == 0) or (self.value % 4 == 0 and self.value % 100 != 0):
            isbissextile = True
        elif (self.value % 4 != 0) or (self.value % 4 == 0 and self.value % 100 == 0 and self.value % 400 != 0):
            isbissextile = False
        return isbissextile

    def __str__(self):
        return str(self.value)


class Archive (models.Model):
    endpoint = models.CharField(max_length=250)
    date = models.CharField(max_length=500)
    result = models.TextField()

    def __str__(self):
        return f"{self.endpoint} {self.date} {self.result}"
