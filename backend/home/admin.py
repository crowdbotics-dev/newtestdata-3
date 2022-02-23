from django.contrib import admin
from .models import Test, Testcheck, Testingsaap, Testnews

admin.site.register(Testingsaap)
admin.site.register(Testnews)
admin.site.register(Testcheck)
admin.site.register(Test)

# Register your models here.
