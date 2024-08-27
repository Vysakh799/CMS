# Generated by Django 5.0.6 on 2024-08-27 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_admin_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semno', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.TextField()),
                ('aname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.admins')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.TextField()),
                ('staffemail', models.TextField()),
                ('staffphno', models.TextField()),
                ('staffaddress', models.TextField()),
                ('staffpassword', models.TextField()),
                ('aname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.admins')),
                ('staffbranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branches')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.TextField()),
                ('stregno', models.TextField()),
                ('stadmno', models.TextField()),
                ('stemail', models.TextField()),
                ('stphno', models.TextField()),
                ('staddress', models.TextField()),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branches')),
                ('ssem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sem')),
                ('staffname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.TextField()),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branches')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sem')),
            ],
        ),
        migrations.CreateModel(
            name='Semexam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branches')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sem')),
                ('stname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('subname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
    ]
