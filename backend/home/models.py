from django.conf import settings
from django.db import models


class Testingsaap(models.Model):
    "Generated Model"
    testedapp = models.TimeField()
    checktest = models.SlugField(
        max_length=50,
    )
