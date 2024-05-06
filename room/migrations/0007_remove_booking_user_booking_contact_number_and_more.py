# Generated by Django 5.0.2 on 2024-05-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_remove_booking_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='contact_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
