# Generated by Django 5.0.1 on 2024-02-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_profile_facebook_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='codeforces_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
