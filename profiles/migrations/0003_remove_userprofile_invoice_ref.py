# Generated by Django 3.2.23 on 2024-02-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='invoice_ref',
        ),
    ]