# Generated by Django 3.1.7 on 2021-11-19 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faktury', '0002_auto_20211119_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_invoice',
            name='total_price',
        ),
    ]
