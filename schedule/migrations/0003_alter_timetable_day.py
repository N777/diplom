# Generated by Django 4.1.3 on 2023-04-07 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_weekdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.weekdays'),
        ),
    ]
