# Generated by Django 3.0.2 on 2020-03-07 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyroom', '0006_auto_20200307_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takenquiz',
            name='correct',
        ),
    ]
