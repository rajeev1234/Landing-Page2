# Generated by Django 2.0.3 on 2018-03-31 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRecceTourGuide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmreccetourguide',
            name='FilmRecceTourGuide_Message',
        ),
        migrations.AlterField(
            model_name='filmreccetourguide',
            name='FilmRecceTourGuide_Created_Time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='filmreccetourguide',
            name='FilmRecceTourGuide_Modified_Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
