# Generated by Django 5.0.1 on 2024-01-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcafe', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_price',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=5),
            preserve_default=False,
        ),
    ]