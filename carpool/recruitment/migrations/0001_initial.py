# Generated by Django 3.1.3 on 2022-02-04 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('car_num', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=100)),
                ('max_num', models.CharField(max_length=10)),
                ('present_num', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]