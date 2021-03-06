# Generated by Django 3.1.2 on 2020-10-27 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spotting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('time_of_day', models.CharField(choices=[('DWN', 'Dawn'), ('MRN', 'Morning'), ('AFT', 'Afternoon'), ('DSK', 'Dusk'), ('NIT', 'Night')], default='DWN', max_length=3)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bird')),
            ],
        ),
    ]
