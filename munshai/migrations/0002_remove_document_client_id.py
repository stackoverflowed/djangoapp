# Generated by Django 2.1.2 on 2018-11-07 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('munshai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='client_id',
        ),
    ]