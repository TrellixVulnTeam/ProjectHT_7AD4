# Generated by Django 2.2.7 on 2019-11-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20191128_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharestory',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
