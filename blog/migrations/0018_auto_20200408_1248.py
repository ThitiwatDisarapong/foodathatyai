# Generated by Django 3.0.3 on 2020-04-08 05:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200408_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='closeday',
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('อาหารใต้', 'อาหารใต้'), ('อาหารเหนือ', 'อาหารเหนือ'), ('อาหารอีสาน', 'อาหารอีสาน')], default='อาหารทั่วไป', max_length=30),
        ),
    ]
