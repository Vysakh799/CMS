# Generated by Django 5.0.6 on 2024-08-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_semexam'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='setnewpsw',
            field=models.BooleanField(default=False),
        ),
    ]
