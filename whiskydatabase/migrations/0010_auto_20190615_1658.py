# Generated by Django 2.1.7 on 2019-06-15 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0009_whiskyinfo_bottling'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whiskyinfo',
            name='distillery',
        ),
        migrations.AddField(
            model_name='whiskyinfo',
            name='distillery',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='whisky_distillery', to='whiskydatabase.Distillery'),
            preserve_default=False,
        ),
    ]