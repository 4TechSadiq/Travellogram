# Generated by Django 5.1.1 on 2024-10-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=500)),
                ('picture', models.CharField(max_length=2500)),
                ('description', models.CharField(max_length=1500)),
                ('country', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('weather', models.CharField(max_length=500)),
                ('activity', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=1500)),
            ],
        ),
    ]
