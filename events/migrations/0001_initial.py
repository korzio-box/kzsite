# Generated by Django 3.1.1 on 2021-07-29 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_add', models.DateTimeField()),
                ('time_done', models.DateTimeField()),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Planowane'), (2, 'Wykonane')])),
                ('Product', models.ManyToManyField(blank=True, to='warehouse.Product')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.client')),
            ],
        ),
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.product')),
            ],
        ),
    ]