# Generated by Django 2.2.5 on 2019-10-01 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
    ]
