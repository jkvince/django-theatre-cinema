# Generated by Django 5.1.7 on 2025-04-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_showmember_shows_delete_memberjunction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_banner',
            field=models.ImageField(upload_to='shows/'),
        ),
    ]
