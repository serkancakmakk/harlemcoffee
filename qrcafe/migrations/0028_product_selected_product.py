# Generated by Django 5.0.1 on 2024-02-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcafe', '0027_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selected_product',
            field=models.BooleanField(default='False'),
        ),
    ]