# Generated by Django 2.0.3 on 2018-03-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCatagory', '0005_remove_servicecatagory_servicecatagory_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecatagory',
            name='ServiceCatagory_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
