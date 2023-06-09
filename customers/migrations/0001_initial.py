# Generated by Django 3.2.12 on 2023-04-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('plane_id', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('booked_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('seat_type', models.CharField(max_length=100)),
                ('seat_no', models.IntegerField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]
