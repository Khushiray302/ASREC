# Generated by Django 5.0.3 on 2024-03-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('msgdate', models.DateField(null=True)),
                ('isread', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
