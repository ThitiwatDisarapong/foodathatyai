# Generated by Django 2.2.7 on 2020-02-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200220_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]
