# Generated by Django 5.0.3 on 2024-03-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_blog_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='video_file',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
