# Generated by Django 2.1.7 on 2019-06-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0002_auto_20190611_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalwhiskynote',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='personalwhiskynote',
            name='rating',
        ),
        migrations.AddField(
            model_name='note',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]