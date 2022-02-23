from django.contrib import admin
from .models import Test, Testcheck, Testingsaap, Testnews, Ytest

admin.site.register(Testingsaap)
admin.site.register(Testnews)
admin.site.register(Testcheck)
admin.site.register(Test)
admin.site.register(Ytest)

# Register your models here.
