# Generated by Django 5.0.2 on 2024-05-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_remove_room_description_room_available_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='available_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
