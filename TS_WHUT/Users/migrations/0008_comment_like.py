# Generated by Django 2.0.5 on 2018-07-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_folder_nums'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]