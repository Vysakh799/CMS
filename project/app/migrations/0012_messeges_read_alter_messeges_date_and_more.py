# Generated by Django 5.0.6 on 2024-09-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_messeges'),
    ]

    operations = [
        migrations.AddField(
            model_name='messeges',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='messeges',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='messeges',
            name='time',
            field=models.TimeField(),
        ),
    ]
