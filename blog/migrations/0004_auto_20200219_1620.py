# Generated by Django 2.2.7 on 2020-02-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parking',
            field=models.CharField(choices=[('มี', 'มี'), ('ไม่มี', 'ไม่มี')], default='มี', max_length=6),
        ),
        migrations.AddField(
            model_name='post',
            name='wifi',
            field=models.CharField(choices=[('มี', 'มี'), ('ไม่มี', 'ไม่มี')], default='มี', max_length=6),
        ),
    ]
