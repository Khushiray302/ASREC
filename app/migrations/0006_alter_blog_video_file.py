# Generated by Django 5.0.3 on 2024-03-29 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_video_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='video_file',
            field=models.BinaryField(),
        ),
    ]