# Generated by Django 5.0.2 on 2024-05-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='room',
            name='available_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
