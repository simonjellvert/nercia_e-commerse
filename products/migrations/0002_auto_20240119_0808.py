# Generated by Django 3.2.23 on 2024-01-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcontent',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Description of the training'),
        ),
    ]
