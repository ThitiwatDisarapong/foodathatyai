# Generated by Django 2.2.7 on 2020-02-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highprice',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='post',
            name='lowprice',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
    ]