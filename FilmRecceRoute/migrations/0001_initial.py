# Generated by Django 2.0.3 on 2018-03-26 05:25

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
                ('FilmRecceRoute_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FilmRecceRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilmRecceRoute_Distance', models.CharField(max_length=100)),
                ('FilmRecceRoute_Filmrecce_Name', models.CharField(max_length=100)),
                ('FilmRecceRoute_Route_Name', models.CharField(max_length=100)),
                ('FilmRecceRoute_Travel_Time', models.CharField(max_length=100)),
                ('FilmRecceRoute_Modified_Date', models.DateField()),
                ('FilmRecceRoute_Created_Date', models.DateField()),
                ('FilmRecceRoute_Message', models.CharField(max_length=280)),
                ('FilmRecceRoute_Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FilmRecceRoutes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_FilmRecceRoute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFilmRecceRoute', to='FilmRecceRoute.FilmRecceRoute'),
        ),
        migrations.AddField(
            model_name='comment',
            name='FilmRecceRoute_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssFilmRecceRoute', to=settings.AUTH_USER_MODEL),
        ),
    ]