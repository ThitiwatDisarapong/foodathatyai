# Generated by Django 3.0.3 on 2020-04-08 12:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('อาหารใต้', 'อาหารใต้'), ('อาหารเหนือ', 'อาหารเหนือ'), ('อาหารอีสาน', 'อาหารอีสาน')], max_length=30)),
            ],
        ),
    ]
