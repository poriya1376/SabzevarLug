# Generated by Django 3.0.5 on 2020-05-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200528_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='raouf',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='app/static/img/post'),
        ),
    ]