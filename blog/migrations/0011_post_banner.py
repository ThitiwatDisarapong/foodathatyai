# Generated by Django 2.2.7 on 2020-02-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200220_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Banner',
            field=models.ImageField(default='default.jpg', upload_to='menu_pics'),
        ),
    ]