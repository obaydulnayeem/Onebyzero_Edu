# Generated by Django 5.0.1 on 2024-01-24 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_pendingusermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingusermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]