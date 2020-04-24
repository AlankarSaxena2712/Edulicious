from django.contrib import admin
from django.contrib.auth.models import User
from .models import PhoneSave

# Register your models here.
admin.site.site_header = "EDULICIOUS"
admin.site.register(PhoneSave)

class User(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email')


class PhomeSave(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'timestamp')