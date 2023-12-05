from django.db import models


class Profiles(models.Model):
     name=models.CharField(max_length=200)
     cookies=models.TextField()
     proxies=models.TextField()
    