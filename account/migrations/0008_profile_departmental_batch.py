# Generated by Django 5.0.1 on 2024-01-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_pendingusermodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='departmental_batch',
            field=models.CharField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th')], default='*st', max_length=50),
        ),
    ]
