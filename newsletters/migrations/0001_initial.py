# Generated by Django 3.2.23 on 2024-02-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('content', models.TextField()),
                ('newsletter_category', models.CharField(choices=[('general', 'General'), ('promotions', 'Promotions'), ('product_updates', 'Product Updates')], default='general', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
