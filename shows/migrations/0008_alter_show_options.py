# Generated by Django 5.1.7 on 2025-04-20 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0007_alter_show_show_release_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ['show_name']},
        ),
    ]
