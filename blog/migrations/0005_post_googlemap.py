# Generated by Django 2.2.7 on 2020-02-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200219_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='googlemap',
            field=models.CharField(default='www.google.com', max_length=999999),
        ),
    ]
