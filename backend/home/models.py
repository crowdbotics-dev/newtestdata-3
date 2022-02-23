from django.conf import settings
from django.db import models


class Testingsaap(models.Model):
    "Generated Model"
    testedapp = models.TimeField()
    checktest = models.SlugField(
        max_length=50,
    )


class Testnews(models.Model):
    "Generated Model"
    yestest = models.URLField()
    oktest = models.TextField()


class Testcheck(models.Model):
    "Generated Model"
    testapps = models.URLField()
    oktestnew = models.TextField()


class Test(models.Model):
    "Generated Model"
    eee = models.URLField()
    ee = models.TimeField()
