from django.db import models

# Create your models here.

class PhoneSave(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    phone_number = models.BigIntegerField(blank=False)
    stud_class = models.IntegerField(blank=False, default=1)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name