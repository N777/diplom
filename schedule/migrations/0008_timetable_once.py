# Generated by Django 4.1.3 on 2023-05-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_timetable_group_alter_timetable_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='once',
            field=models.BooleanField(default=False),
        ),
    ]