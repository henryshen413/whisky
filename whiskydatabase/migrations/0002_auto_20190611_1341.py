# Generated by Django 2.1.7 on 2019-06-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distillery',
            name='owner',
            field=models.CharField(default='owner', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalwhiskynote',
            name='salty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personalwhiskynote',
            name='salty',
            field=models.CharField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, max_length=1),
            preserve_default=False,
        ),
    ]