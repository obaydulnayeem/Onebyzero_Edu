# Generated by Django 5.0.1 on 2024-01-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0010_alter_lecturemodel_session_alter_notemodel_session_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='hour',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
