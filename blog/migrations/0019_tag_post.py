# Generated by Django 3.0.3 on 2020-04-08 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200408_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='blog.Post'),
        ),
    ]
