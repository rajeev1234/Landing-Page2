# Generated by Django 2.0.3 on 2018-03-26 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCatagory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comment_FilmRecceTourGuide',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='FilmRecceTourGuide_Comment_Author',
        ),
        migrations.RemoveField(
            model_name='filmreccetourguide',
            name='FilmRecceTourGuide_Creator',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='FilmRecceTourGuide',
        ),
    ]