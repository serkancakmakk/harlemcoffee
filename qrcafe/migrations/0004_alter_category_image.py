# Generated by Django 5.0.1 on 2024-01-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcafe', '0003_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='static/image/category_image'),
        ),
    ]