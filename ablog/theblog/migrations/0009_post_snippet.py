# Generated by Django 3.1.4 on 2021-01-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_auto_20210111_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='go to post', max_length=255),
        ),
    ]
