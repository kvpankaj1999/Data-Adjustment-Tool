# Generated by Django 3.0.6 on 2020-05-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('stud_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('valid_from', models.DateField(auto_now_add=True)),
                ('valid_to', models.DateField(auto_now=True)),
                ('latest', models.BooleanField()),
            ],
        ),
    ]
