# Generated by Django 2.2.7 on 2019-11-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191126_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='publish',
            new_name='created',
        ),
    ]
