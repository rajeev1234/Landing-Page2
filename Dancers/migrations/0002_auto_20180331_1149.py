# Generated by Django 2.0.3 on 2018-03-31 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dancers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comment_Dancer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Dancer_Comment_Author',
        ),
        migrations.RemoveField(
            model_name='dancer',
            name='Dancer_Creator',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Dancer',
        ),
    ]
