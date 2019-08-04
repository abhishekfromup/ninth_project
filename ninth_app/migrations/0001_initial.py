# Generated by Django 2.0.5 on 2019-08-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=30)),
                ('student_email', models.EmailField(max_length=30)),
                ('student_date_of_birth', models.DateTimeField()),
                ('student_mobile', models.CharField(max_length=12)),
            ],
        ),
    ]
