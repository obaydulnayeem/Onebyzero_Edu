# Generated by Django 5.0.1 on 2024-02-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default.png', null=True, upload_to='profile_images/'),
        ),
    ]