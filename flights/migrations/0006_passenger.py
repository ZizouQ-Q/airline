# Generated by Django 3.0.6 on 2020-05-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20200515_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
