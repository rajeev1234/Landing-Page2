# Generated by Django 2.0.3 on 2018-03-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCatagory', '0003_auto_20180326_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecatagory',
            name='ServiceCatagory_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]