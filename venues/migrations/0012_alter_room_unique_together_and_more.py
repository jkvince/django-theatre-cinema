# Generated by Django 5.1.7 on 2025-04-01 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0011_alter_room_room_columns_alter_room_room_rows_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set(),
        ),
    ]
