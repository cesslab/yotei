# Generated by Django 2.2.6 on 2019-10-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'MANAGER'), (2, 'RESEARCHER'), (3, 'SUBJECT')], default=1, verbose_name='role'),
            preserve_default=False,
        ),
    ]
