# Generated by Django 2.2.6 on 2019-11-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clanbattle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentboss',
            name='loop_count',
            field=models.IntegerField(default=1, verbose_name='週'),
        ),
    ]
