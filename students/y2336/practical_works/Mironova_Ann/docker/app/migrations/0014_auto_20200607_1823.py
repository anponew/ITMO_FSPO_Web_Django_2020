# Generated by Django 3.0.6 on 2020-06-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200607_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id_crew_member1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crew_member1', to='app.crew_member'),
        ),
    ]
