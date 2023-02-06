# Generated by Django 3.2.16 on 2023-02-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('teacher_code', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=False)),
                ('join_date', models.DateField()),
                ('working_days', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]