from django.db import models


class Status(models.Model):
     keyword=models.CharField(max_length=20000)
    