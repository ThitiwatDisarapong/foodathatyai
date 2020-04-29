# Generated by Django 3.0.3 on 2020-04-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200426_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_chinesefood',
            field=models.BooleanField(default=False, verbose_name='อาหารจีน'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_japanfood',
            field=models.BooleanField(default=False, verbose_name='อาหารญี่ปุ่น'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_thaifood',
            field=models.BooleanField(default=False, verbose_name='อาหารไทย'),
        ),
    ]