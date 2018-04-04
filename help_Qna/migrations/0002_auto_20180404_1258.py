# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help_Qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpqna',
            name='Help_Qna_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpqna', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Qna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_Qna.HelpQna'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Qna_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentqna', to=settings.AUTH_USER_MODEL),
        ),
    ]