# Generated by Django 4.2 on 2024-01-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_order', '0011_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
