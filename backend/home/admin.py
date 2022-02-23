from django.contrib import admin
from .models import Testcheck, Testingsaap, Testnews

admin.site.register(Testingsaap)
admin.site.register(Testnews)
admin.site.register(Testcheck)

# Register your models here.
