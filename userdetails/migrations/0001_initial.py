# Generated by Django 2.0.3 on 2018-04-04 07:28

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
                ('UserDetails_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserDetails_UserDetails_Message', models.CharField(max_length=280)),
                ('UserDetails_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('UserDetails_Address', models.CharField(max_length=200)),
                ('UserDetails_City', models.CharField(max_length=200)),
                ('UserDetails_Completed', models.BooleanField(default=True)),
                ('UserDetails_Country', models.CharField(max_length=200)),
                ('UserDetails_Date_Of_Birth', models.DateField()),
                ('UserDetails_First_Name', models.CharField(max_length=200)),
                ('UserDetails_Gender', models.CharField(max_length=200)),
                ('UserDetails_Last_Name', models.CharField(max_length=200)),
                ('UserDetails_Phone', models.IntegerField(default=-1)),
                ('UserDetails_Pin_Code', models.IntegerField(default=-1)),
                ('UserDetails_Street_Address', models.CharField(max_length=200)),
                ('UserDetails_User_Description', models.CharField(max_length=200)),
                ('UserDetails_User_ID', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_UserDetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails_Comment', to='userdetails.UserDetails'),
        ),
        migrations.AddField(
            model_name='comment',
            name='UserDetails_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetailss', to=settings.AUTH_USER_MODEL),
        ),
    ]
