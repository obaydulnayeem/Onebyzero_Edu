# Generated by Django 5.0.1 on 2024-02-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_profile_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]
