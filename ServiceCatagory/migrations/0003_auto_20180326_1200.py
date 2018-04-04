# Generated by Django 2.0.3 on 2018-03-26 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServiceCatagory', '0002_auto_20180326_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceCatagory_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceCatagory_Icon_Number', models.IntegerField()),
                ('ServiceCatagory_Image', models.ImageField(upload_to='')),
                ('ServiceCatagory_Responsibilities', models.CharField(max_length=200)),
                ('ServiceCatagory_Service_Category', models.CharField(max_length=200)),
                ('ServiceCatagory_What_Do_You_Do', models.CharField(max_length=200)),
                ('ServiceCatagory_Message', models.CharField(max_length=280)),
                ('ServiceCatagory_Users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_ServiceCatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsServiceCatagory', to='ServiceCatagory.ServiceCatagory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ServiceCatagory_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssServiceCatagory', to=settings.AUTH_USER_MODEL),
        ),
    ]