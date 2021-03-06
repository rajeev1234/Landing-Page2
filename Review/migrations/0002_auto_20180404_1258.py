# Generated by Django 2.0.3 on 2018-04-04 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Review_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentReview', to='Review.Review'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Review_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AuthorcommentReview', to=settings.AUTH_USER_MODEL),
        ),
    ]
