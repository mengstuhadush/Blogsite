# Generated by Django 4.2 on 2023-12-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_order', '0004_alter_product_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customer_email',
            field=models.EmailField(max_length=255),
        ),
    ]
