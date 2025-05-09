# Generated by Django 5.1.7 on 2025-03-24 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.SlugField(primary_key=True, serialize=False)),
                ('venue_name', models.CharField(max_length=30)),
                ('venue_address', models.CharField(max_length=30)),
                ('venue_accessibility', models.BooleanField()),
                ('working_hours', models.CharField(max_length=10)),
                ('venue_latitude', models.FloatField()),
                ('venue_longitude', models.FloatField()),
                ('venue_contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.SlugField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=15)),
                ('seat_layout', models.FileField(upload_to='')),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.venue')),
            ],
            options={
                'unique_together': {('room_number', 'venue_id')},
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.SlugField(primary_key=True, serialize=False)),
                ('seat_number', models.CharField(max_length=10)),
                ('seat_premium', models.BooleanField()),
                ('seat_accessible', models.BooleanField()),
                ('seat_price', models.FloatField()),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.room')),
            ],
            options={
                'unique_together': {('seat_number', 'room_number')},
            },
        ),
    ]
