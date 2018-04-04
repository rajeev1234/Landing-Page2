# Generated by Django 2.0.3 on 2018-03-26 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilmRecceTourGuide_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FilmRecceTourGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilmRecceTourGuide_EndLocation', models.CharField(max_length=200)),
                ('FilmRecceTourGuide_EndTime', models.DateField()),
                ('FilmRecceTourGuide_Passing_Year', models.CharField(max_length=100)),
                ('FilmRecceTourGuide_StartLocation', models.CharField(max_length=100)),
                ('FilmRecceTourGuide_StartTime', models.DateField()),
                ('FilmRecceTourGuide_TourGuideName', models.CharField(max_length=100)),
                ('FilmRecceTourGuide_Modified_Date', models.DateField()),
                ('FilmRecceTourGuide_Created_Time', models.DateField()),
                ('FilmRecceTourGuide_Message', models.CharField(max_length=280)),
                ('FilmRecceTourGuide_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FilmRecceRoutesGuide', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_FilmRecceTourGuide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFilmRecceTourGuide', to='FilmRecceTourGuide.FilmRecceTourGuide'),
        ),
        migrations.AddField(
            model_name='comment',
            name='FilmRecceTourGuide_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssFilmRecceTourGuide', to=settings.AUTH_USER_MODEL),
        ),
    ]