# Generated by Django 5.0.1 on 2024-02-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcafe', '0024_category_created_time_alter_category_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_time',
            field=models.DurationField(),
        ),
    ]