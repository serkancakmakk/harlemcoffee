# Generated by Django 5.0.1 on 2024-01-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcafe', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
