# Generated by Django 3.2.23 on 2024-01-26 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
