# Generated by Django 5.1.7 on 2025-04-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_alter_show_public_alter_show_show_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_duration',
            field=models.IntegerField(help_text='Duration in minutes'),
        ),
    ]
