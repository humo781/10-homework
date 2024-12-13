# Generated by Django 5.1.4 on 2024-12-13 06:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]