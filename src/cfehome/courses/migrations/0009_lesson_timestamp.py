# Generated by Django 5.1.2 on 2024-11-11 19:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_lesson_options_lesson_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]