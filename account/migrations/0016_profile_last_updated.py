# Generated by Django 5.0.1 on 2024-02-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_profile_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
