# Generated by Django 3.0.5 on 2020-04-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_phonesave_stud_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonesave',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
