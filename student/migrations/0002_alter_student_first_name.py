# Generated by Django 3.2.16 on 2023-02-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
