from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=10, default='')
    query = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class CLass_1(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_2(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_3(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_4(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_5(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_6(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_7(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_8(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_9(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name

class CLass_10(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_link = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name