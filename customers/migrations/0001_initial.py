# Generated by Django 3.1.1 on 2021-07-05 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('tel_number', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{9}$')])),
                ('Hair', models.IntegerField(blank=True, choices=[('1', 'Długie'), ('2', 'Pół-długie'), ('3', 'Krótkie')], max_length=1)),
            ],
        ),
    ]
