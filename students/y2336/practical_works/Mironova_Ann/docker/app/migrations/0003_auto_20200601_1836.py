# Generated by Django 3.0.6 on 2020-06-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_of_appointment_of_the_pilot_on_the_helicopter',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='login',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
