# Generated by Django 4.0.6 on 2022-07-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=512)),
                ('lastname', models.CharField(max_length=512)),
                ('birth_date', models.DateField()),
                ('GPA', models.FloatField()),
            ],
        ),
    ]
