# Generated by Django 5.0.1 on 2024-02-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0022_alter_bookmodel_semester_alter_bookmodel_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st Semester'), ('2nd', '2nd Semester'), ('3rd', '3rd Semester'), ('4th', '4th Semester'), ('5th', '5th Semester'), ('6th', '6th Semester'), ('7th', '7th Semester'), ('8th', '8th Semester')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='year',
            field=models.CharField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], max_length=5, null=True),
        ),
    ]
