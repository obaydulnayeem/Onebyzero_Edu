# Generated by Django 5.0.1 on 2024-02-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_profile_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='semester',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1st'), (2, '2nd')], null=True),
        ),
    ]
